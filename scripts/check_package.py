"""Dependency-free package checks; not a behavioral coaching evaluation."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check():
    folder = ROOT / "skills" / "consulting-portfolio-coach"
    skill = (folder / "SKILL.md").read_text(encoding="utf-8")
    front = skill.split("---", 2)[1]
    assert "name: consulting-portfolio-coach" in front
    assert "description:" in front
    for match in re.findall(r"`((?:references|templates)/[^`]+)`", skill):
        assert (folder / match).exists(), match
    assert (folder / "references" / "scheduling.md").exists()
    assert len(list((folder / "templates").glob("*.md"))) == 5
    assert (folder / "agents" / "openai.yaml").exists()
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "__pycache__" in path.parts or not path.is_file():
            continue
        if path.suffix not in (".md", ".py", ".yaml", ".yml"):
            continue
        text = path.read_text(encoding="utf-8")
        assert not re.search("/" + r"Users/[^/\s]+/", text), f"Personal path in {path}"
        assert not re.search(r"sk-(?:or-v1-)?[A-Za-z0-9]{20,}", text), f"Possible secret in {path}"
    print("Package structure, references and basic privacy checks passed.")


if __name__ == "__main__":
    check()
