#!/usr/bin/env python3
import random


def main():
    Players = [
            'Alice', 'bob', 'Charlie', 'dylan',
            'Emma', 'Gregory', 'john', 'kevin', 'Liam'
            ]
    print(f"Initial list of players: {Players}")
    Cap_Players = [name.capitalize() for name in Players]
    Cap_only_Players = [name for name in Players if name[0].isupper()]
    print(f"New list with all names capitalized: {Cap_Players}")
    print(f"New list of capitalized names only: {Cap_only_Players}")
    Score_Dict = {name: random.randrange(1, 1000) for name in Cap_Players}
    Score_Sum = 0
    for name in Score_Dict:
        Score_Sum += Score_Dict[name]
    # High_Score = {name }
    print(f"\nScore dict: {Score_Dict}")
    Score_Avr = round(Score_Sum / len(Score_Dict), 2)
    print(f"Score average is {Score_Avr}")
    High_Score = {name: Score_Dict[name] for
                  name in Score_Dict if Score_Dict[name] > Score_Avr}
    print(f"High scores: {High_Score}")


if __name__ == "__main__":
    main()
