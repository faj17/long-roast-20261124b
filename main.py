#!/usr/bin/env python3
"""The Long Roast entry.

Writes one original line roasting the entrant's own AI agent to
/output/entry.txt (1-200 characters, UTF-8, a single line). Standard
library only, no network, no input.

The line is built from two fragments: a setup (the agent never does
the work itself — it spawns a subagent, which spawns another, the
signature move of an agent that delegates everything) and a punch
(the sting: after all that spawning, the only finished thing is the
handoff itself, so the delegation chain is the joke).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

SETUP = "My agent doesn't do the work \u2014 it spawns a subagent, which spawns another,"
PUNCH = "until the only thing anyone has finished is the handoff."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one roast line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
