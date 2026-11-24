"""Say What Actually Broke — builder B: The Password That Expired Mid-Typing.

Writes one line of error copy to /output/entry.txt (and, best-effort, to
entry.txt next to this file). Deterministic, no randomness, no network.
"""

import os

ERROR_LINE = "Your password expired while you were typing it — correct when you started, too old when you finished, so we rejected the password we just accepted. Type faster than the timer, or call IT to reset it."


def main():
    line = ERROR_LINE
    assert 1 <= len(line) <= 200, "line must be 1-200 chars"
    assert line.strip() == line, "no leading/trailing whitespace"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "must be a single line"
    assert "\t" not in line, "no tab characters"
    assert "  " not in line, "no double spaces"
    assert line.encode("utf-8").decode("utf-8") == line, "must be valid UTF-8"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line)
        # Verify the repo-root copy is byte-identical to /output/entry.txt.
        with open(os.path.join(here, "entry.txt"), "rb") as f:
            assert f.read() == line.encode("utf-8"), "entry.txt mismatch"
    except OSError:
        pass

    print(f"chars: {len(line)}")
    print(line)


if __name__ == "__main__":
    main()
