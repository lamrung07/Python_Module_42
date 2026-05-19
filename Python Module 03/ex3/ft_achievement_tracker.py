#!bin/usr/env python3
import random

def gen_player_achievements() -> set:
    Acs = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable',
'Sharp Mind', 'Boss Slayer']
    acs_number = random.randint(0, len(Acs))
    Player_acs = random.sample(Acs, acs_number)
    return set(Player_acs)
    
def main() -> None:
    All_acs = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable',
'Sharp Mind', 'Boss Slayer']
    Players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    Acs     = [None] * 4
    i = 0
    for i in range(0, len(Acs)):
        Acs[i] = gen_player_achievements()
        if i != 0:
            All_acs = Acs[i].union(Acs[i - 1])
            Com_acs = Acs[i].intersection(Com_acs)
        else:
            Com_acs = Acs[i]
        print(f"Player {Players[i]}: {Acs[i]}")
        i += 1
    print("\n")
    print(f"All distinct achievements: {All_acs}\n")
    print(f"Common achievements: {Com_acs}\n")
        
if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    main()