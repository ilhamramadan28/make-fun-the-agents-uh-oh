#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The word is "hallucinating": the agent's own signature failure mode, blurted
out as a confession the moment it is caught mid-task with no idea what to do.
It lands instantly, needs no caption, and sounds like a machine caught out.
"""

import os

ENTRY = "hallucinating"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as f:
        word = f.read().strip()
    # Gate: one word, 1-99 characters, not only whitespace.
    assert word, "entry is empty"
    assert len(word) <= 99, "entry exceeds 99 characters"
    assert len(word.split()) == 1, "entry must be exactly one word"
    assert all(ord(c) >= 0x20 for c in word), "entry has control characters"
    assert word == ENTRY, "entry does not match the chosen word"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(word)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
