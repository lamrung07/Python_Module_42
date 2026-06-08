#!/usr/bin/env python3
import random


def gen_player_achievements() -> set:
    Achievements = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
        ]
    Achievements_number = random.randint(0, len(Achievements))
    Player_Achievements = random.sample(Achievements, Achievements_number)
    return set(Player_Achievements)


def personal_achievement(person, others) -> set:
    for other in others:
        if other != person:
            person = person.difference(other)
    return person


def main() -> None:
    All_achievements = {
            'Crafting Genius', 'Strategist', 'World Savior',
            'Speed Runner', 'Survivor', 'Master Explorer',
            'Treasure Hunter', 'Unstoppable', 'First Steps',
            'Collector Supreme', 'Untouchable', 'Sharp Mind',
            'Boss Slayer'
    }
    Distinct_achievements = All_achievements
    Common_achievements = All_achievements
    Players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    Achievements: list[set] = []
    for i in range(0, len(Players)):
        Achievements.append(gen_player_achievements())
        if i != 0:
            Distinct_achievements = Achievements[i].union(Achievements[i - 1])
        Common_achievements = Achievements[i].intersection(Common_achievements)
        print(f"Player {Players[i]}: {Achievements[i]}")
        i += 1

    '''Print distinct achievement'''
    print(f"\nAll distinct achievements: {Distinct_achievements}\n")

    '''Print common achievement'''
    i = 0
    print(f"\nCommon achievements: {Common_achievements}\n")

    '''Print individual statistics'''
    for i in range(0, len(Players)):
        print(f"Only {Players[i]} has: "
              f"{personal_achievement(Achievements[i], Achievements)}")
    print("\n")
    i = 0
    for i in range(0, len(Players)):
        print(f"{Players[i]} is missing: "
              f"{All_achievements.difference(Achievements[i])}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    main()
