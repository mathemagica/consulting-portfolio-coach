import importlib.util
import os
import stat
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("setup", Path(__file__).resolve().parents[1] / "scripts" / "setup.py")
setup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(setup)


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        # macOS temp directories may contain a system symlink; use their real path.
        self.root = Path(self.temp.name).resolve()

    def tearDown(self):
        self.temp.cleanup()

    def test_both_clients_receive_complete_identical_skills(self):
        destinations = setup.install("both", self.root)
        for dest in destinations:
            for source in setup.SKILL.rglob("*"):
                if source.is_file():
                    self.assertEqual(source.read_bytes(), (dest / source.relative_to(setup.SKILL)).read_bytes())

    def test_reinstall_identical_is_safe(self):
        first = setup.install("both", self.root)
        self.assertEqual(first, setup.install("both", self.root))

    def test_conflict_preserves_local_changes_and_other_client(self):
        destination = setup.install("claude", self.root)[0]
        (destination / "SKILL.md").write_text("local changes")
        with self.assertRaises(ValueError):
            setup.install("both", self.root)
        self.assertEqual((destination / "SKILL.md").read_text(), "local changes")
        self.assertFalse((self.root / ".agents").exists())

    def test_extra_private_file_stops_reinstall(self):
        destination = setup.install("codex", self.root)[0]
        (destination / "notes.md").write_text("private")
        with self.assertRaises(ValueError):
            setup.install("codex", self.root)

    def test_workspace_creates_only_blank_private_notes(self):
        workspace = setup.init_workspace(self.root / "notes")
        self.assertEqual(len(list(workspace.glob("*.md"))), 5)
        self.assertIn("*", (workspace / ".gitignore").read_text())
        if os.name == "posix":
            self.assertEqual(stat.S_IMODE(workspace.stat().st_mode), 0o700)
            self.assertEqual(stat.S_IMODE((workspace / "profile.md").stat().st_mode), 0o600)

    def test_workspace_never_overwrites(self):
        workspace = setup.init_workspace(self.root / "notes")
        (workspace / "profile.md").write_text("my profile")
        with self.assertRaises(ValueError):
            setup.init_workspace(workspace)
        self.assertEqual((workspace / "profile.md").read_text(), "my profile")

    def test_git_directory_and_worktree_are_refused(self):
        for name, is_file in (("repo", False), ("worktree", True)):
            repo = self.root / name
            repo.mkdir()
            if is_file:
                (repo / ".git").write_text("gitdir: somewhere")
            else:
                (repo / ".git").mkdir()
            with self.assertRaises(ValueError):
                setup.init_workspace(repo / "notes")

    def test_source_repository_refused_even_before_git_init(self):
        with self.assertRaises(ValueError):
            setup.init_workspace(setup.ROOT / "notes")

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_symlink_workspace_and_install_refused(self):
        target = self.root / "target"
        target.mkdir()
        linked = self.root / "linked"
        linked.symlink_to(target, target_is_directory=True)
        with self.assertRaises(ValueError):
            setup.init_workspace(linked / "notes")
        (self.root / ".agents").symlink_to(target, target_is_directory=True)
        with self.assertRaises(ValueError):
            setup.install("codex", self.root)


if __name__ == "__main__":
    unittest.main()
