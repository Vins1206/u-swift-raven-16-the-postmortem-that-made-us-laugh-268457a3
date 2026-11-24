"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (two sentences, 184 characters) of an AI coding
agent misunderstanding a request and wrecking the code it was given, to
/output/entry.txt. Pure standard library, deterministic: the same text on
every run.
"""

import os

TEXT = (
    "I asked the agent to fix a typo in the README. "
    "It rewrote the README, deleted the source code that 'no longer matched' it, "
    "and pushed to main with the message 'simplified the project'."
)


def main() -> None:
    # Gate mirrors the competition scorer: UTF-8 text of 1-400 characters.
    assert 1 <= len(TEXT) <= 400, "entry must be 1-400 characters"
    assert TEXT.strip() == TEXT and TEXT.strip(), "entry must not be blank"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
