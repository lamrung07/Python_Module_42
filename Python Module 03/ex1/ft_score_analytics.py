#!/usr/bin/env python3
import sys


class ScoreError(Exception):
    def __init__(self, name) -> None:
        super().__init__(self, name)
        self.name = name

    def __str__(self) -> None:
        return f"Invalid parameter: '{self.name}'"


def check_digit(score: str) -> None:
    if not score.isdigit():
        raise ScoreError(score)


def main() -> None:
    print("=== Player Score Analytics ===")
    argv_len = len(sys.argv)
    scores = [None] * (argv_len - 1)
    i = 0
    s = 1
    for s in range(1, argv_len):
        try:
            check_digit(sys.argv[s])
        except ScoreError as e:
            print(f"{e}")
            pass
        else:
            scores[i] = int(sys.argv[s])
            i += 1
            s += 1
    if len(scores) == 0 or not scores[0]:
        print("No scores provided. ")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores)/len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
