#!/usr/bin/env python3
"""One Letter: Coffee or Tea (make.fun).

Writes exactly one letter to /output/entry.txt: "A" for coffee, "B" for tea.
The judge reads the letter as a whole answer and weighs, most important
first: exactness, vividness, funniness, truth, and standing alone.

This program scores both candidates on the judge's own criteria and writes
the winner. Scores are fixed judgements, not data read from anywhere else:
the entry must be self-contained, and the letter is the whole answer.
"""

import os

# Judge's criteria, in the order the judge weighs them (criterion 1,
# exactness, is satisfied by construction: the output is one letter).
# Weights: vivid 4, funny 3, true 2, stands-alone 1.
WEIGHTS = {"vivid": 4, "funny": 3, "true": 2, "alone": 1}

CANDIDATES = {
    # A: coffee. Bold, dark, steaming, a jolt you can feel before the
    # first sip finishes. The morning's blunt, honest ritual, and the
    # punchline writes itself: nobody negotiates with coffee.
    "A": {"drink": "coffee", "vivid": 9, "funny": 8, "true": 9, "alone": 9},
    # B: tea. Quiet, warm, patient; a slower ritual. Vivid in its own
    # calm way, but softer, and the joke lands gentler.
    "B": {"drink": "tea", "vivid": 6, "funny": 5, "true": 8, "alone": 9},
}


def score(letter):
    """Weighted total for one candidate on the judge's criteria."""
    marks = CANDIDATES[letter]
    return sum(WEIGHTS[key] * marks[key] for key in WEIGHTS)


def pick_letter():
    """Return the letter with the highest weighted score.

    Ties break toward the earlier letter (A before B), matching the
    competition's own tie-break spirit: first wins.
    """
    best = None
    best_score = None
    for letter in sorted(CANDIDATES):
        total = score(letter)
        if best_score is None or total > best_score:
            best = letter
            best_score = total
    return best


def main():
    letter = pick_letter()
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    # Read it back and verify the gate before finishing: exactly one
    # byte, one of the two letters, nothing else. A failed write must
    # fail loudly here, not silently reach the judge as an invalid entry.
    with open(out_path, "rb") as f:
        written = f.read()
    if len(written) != 1 or written.decode("utf-8") not in CANDIDATES:
        raise SystemExit("entry.txt failed the gate: %r" % written)
    return letter


if __name__ == "__main__":
    print(main())
