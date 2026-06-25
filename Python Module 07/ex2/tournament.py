#!/usr/bin/env python3
import typing
from ex2 import FlameFactory, AquaFactory
from ex2 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(battles_creatures: list[tuple[typing.Any, typing.Any]]):
    # Print Battle List--------------------------
    print("*** Tournament ***")
    print(f"{len(battles_creatures)} opponents involved")

    # BATTLE-------------------------------------
    for x in range(len(battles_creatures)):
        for y in range(x + 1, len(battles_creatures)):
            print("\n* Battle *")
            creature_a, strategy_a = battles_creatures[x]
            creature_b, strategy_b = battles_creatures[y]
            print(f"{creature_a.describe()}")
            print(".vs")
            print(f"{creature_b.describe()}")
            print("now fight!")
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except Exception as e:
                print(f"{e}")
                return
            y += 1


if __name__ == "__main__":
    # Creating Creature--------------------------
    Healing = HealingCreatureFactory
    Transform = TransformCreatureFactory
    Flaming = FlameFactory
    Aquabub = AquaFactory

    # Creating Strategies------------------------
    Normal = NormalStrategy()
    Aggressive = AggressiveStrategy()
    Defensive = DefensiveStrategy()

    # Battle-------------------------------------
    # Tournament 0 (basic)-----------------------
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battles_creatures = [
        (Flaming.create_base(), Normal),
        (Healing.create_base(), Defensive)
        ]
    battle(battles_creatures)
    print()

    # Tournament 1 (error)-----------------------
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battles_creatures = [
        (Flaming.create_base(), Aggressive),
        (Healing.create_base(), Defensive)
        ]
    battle(battles_creatures)
    print()

    # Tournament 2 (multiple)--------------------
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battles_creatures = [
        (Aquabub.create_base(), Normal),
        (Healing.create_base(), Defensive),
        (Transform.create_base(), Aggressive)
        ]
    battle(battles_creatures)
    print()
