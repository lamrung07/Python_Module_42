#!/usr/bin/env python3
import random


def gen_player_achievements() -> set:
    Acs = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
        ]
    acs_number = random.randint(0, len(Acs))
    Player_acs = random.sample(Acs, acs_number)
    return set(Player_acs)


def personal_achievement(person, others) -> set:
    for other in others:
        if other != person:
            person = person.difference(other)
    return person


def main() -> None:
    All_acs = [
            'Crafting Genius', 'Strategist', 'World Savior',
            'Speed Runner', 'Survivor', 'Master Explorer',
            'Treasure Hunter', 'Unstoppable', 'First Steps',
            'Collector Supreme', 'Untouchable', 'Sharp Mind',
            'Boss Slayer'
    ]
    Dis_acs = All_acs
    Players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    Acs = [None] * len(Players)
    i = 0
    Com_acs = Dis_acs
    for i in range(0, len(Acs)):
        Acs[i] = gen_player_achievements()
        if i != 0:
            Dis_acs = Acs[i].union(Acs[i - 1])
        Com_acs = Acs[i].intersection(Com_acs)
        print(f"Player {Players[i]}: {Acs[i]}")
        i += 1
    print(f"\nAll distinct achievements: {Dis_acs}\n")
    i = 0
    print(f"\nCommon achievements: {Com_acs}\n")
    for i in range(0, len(Players)):
        print(f"Only {Players[i]} has: {personal_achievement(Acs[i], Acs)}")
    print("\n")
    i = 0
    for i in range(0, len(Players)):
        print(f"{Players[i]} is missing: {All_acs.difference(Acs[i])}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    main()
