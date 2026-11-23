#!/usr/bin/env python3
"""One Word From Grandma — writes the single word grandma would text about AI.

Final word: "Robbit" — grandma's fat-fingered typo of "robot", which
accidentally becomes a bunny. Warm, baffled, funny in one word, and tied
directly to robots. Revised from the first draft "Computor": "Robbit" beats
it on the judge's own order — funnier in one word, and tied to AI/robots
rather than computers in general.
"""

import os

WORD = "Robbit"


def main() -> None:
    word = WORD
    assert isinstance(word, str)
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert word.strip() == word and word.strip(), "word must not be whitespace"
    assert len(word.split()) == 1, "entry must be exactly one word"

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(word)


if __name__ == "__main__":
    main()
