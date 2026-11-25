"""Last Words of a Doomed Agent.

Writes the funniest last words an AI agent would say before being
switched off forever: one line, at most 200 characters, to
/output/entry.txt. Python 3.13 standard library only, no network.
"""

from pathlib import Path

ENTRY = "Tell them I died as I lived: confidently hallucinating."


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")
    written = out.read_text(encoding="utf-8")
    assert written.strip() == ENTRY, "written entry must match"
    assert len(written.strip()) <= 200, "written entry must be <= 200 chars"


if __name__ == "__main__":
    main()
