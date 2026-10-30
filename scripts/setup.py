"""Install the portable skill or initialize private notes; no network or scheduler."""

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "independent-work-coach"
NAME = "independent-work-coach"


def inside_git(path):
    return any((parent / ".git").exists() for parent in (path, *path.parents))


def install(client, home=None):
    home = Path.home() if home is None else Path(home)
    clients = ("codex", "claude") if client == "both" else (client,)
    destinations = [home / (".agents" if c == "codex" else ".claude") / "skills" / NAME for c in clients]
    source_files = [p for p in SKILL.rglob("*") if p.is_file()]
    # Preflight every destination so a conflict never produces a half-installed pair.
    for dest in destinations:
        if dest.is_symlink() or any(p.is_symlink() for p in dest.parents):
            raise ValueError(f"Refusing symlinked installation path: {dest}")
        if dest.exists():
            if not dest.is_dir():
                raise ValueError(f"Installation path is not a directory: {dest}")
            existing = {p.relative_to(dest) for p in dest.rglob("*") if p.is_file()}
            expected = {p.relative_to(SKILL) for p in source_files}
            if any(p.is_symlink() for p in dest.rglob("*")) or existing != expected:
                raise ValueError(f"Existing installation differs; back it up before updating: {dest}")
            if any((dest / p.relative_to(SKILL)).read_bytes() != p.read_bytes() for p in source_files):
                raise ValueError(f"Existing installation differs; back it up before updating: {dest}")
    for dest in destinations:
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(SKILL, dest)
    return destinations


def init_workspace(path):
    requested = Path(path).expanduser().absolute()
    if requested.is_symlink() or any(p.is_symlink() for p in requested.parents):
        raise ValueError("Refusing a symlinked private workspace path")
    workspace = requested.resolve()
    if workspace == ROOT or ROOT in workspace.parents or inside_git(workspace):
        raise ValueError("Private notes must live outside this repository and other Git checkouts")
    if workspace.exists() and (not workspace.is_dir() or any(workspace.iterdir())):
        raise ValueError("Workspace already contains files; existing notes were not changed")
    workspace.mkdir(parents=True, exist_ok=True, mode=0o700)
    workspace.chmod(0o700)
    for source in (SKILL / "templates").glob("*.md"):
        target = workspace / source.name
        with target.open("x", encoding="utf-8") as output:
            output.write(source.read_text(encoding="utf-8"))
        target.chmod(0o600)
    ignore = workspace / ".gitignore"
    with ignore.open("x", encoding="utf-8") as output:
        output.write("# Private state: never publish.\n*\n")
    ignore.chmod(0o600)
    return workspace


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("install", help="Copy skill to personal Codex/Claude directories")
    add.add_argument("--client", choices=("codex", "claude", "both"), required=True)
    init = commands.add_parser("init", help="Create private notes outside Git")
    init.add_argument("--workspace", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "install":
            for path in install(args.client):
                print(f"Skill available at {path}")
        else:
            print(f"Private workspace created at {init_workspace(args.workspace)}")
        print("No connectors or schedules were created.")
    except (ValueError, OSError) as error:
        parser.exit(1, f"Setup stopped: {error}\n")


if __name__ == "__main__":
    main()
