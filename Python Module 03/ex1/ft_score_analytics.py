#!bin/usr/env python3
import sys

class ScoreError(Exception):
    def __init__(self, name):
        super().__init__(self, name)
        self.name = name
    def __str__(self):
        return f"Invalid parameter: '{self.name}'"

if __name__ == "__main__":
    ar_len = len(sys.argv)
    scores = []
    i = 0
    try:
        for score in sys.argv:
            if score.isdigit() == False:
                raise ScoreError(score)
            score[i] = score
        i += 1