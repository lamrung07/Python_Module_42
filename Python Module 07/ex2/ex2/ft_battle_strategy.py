#!/usr/bin/env python3
import typing
from abc import ABC, abstractmethod


'''----BattleStrategy abstract class----'''


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: typing.Any) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: typing.Any) -> bool:
        pass


'''Three concrete classes (BattleStrategy)'''


# Only use attack method-------------------------
class NormalStrategy(BattleStrategy):
    def act(self, creature: typing.Any) -> None:
        if self.is_valid(creature):
            print(f"{creature.attack()}")
        else:
            raise Exception(f"Battle error, aborting tournament: "
                            f"Invalid Creature '{type(creature).__name__}' "
                            f"for this aggressive strategy")

    def is_valid(self, creature: typing.Any) -> bool:
        try:
            creature.attack
            return True
        except AttributeError:
            return False


# Creature with transform capabilities-----------
class AggressiveStrategy(BattleStrategy):
    def act(self, creature: typing.Any) -> None:
        if self.is_valid(creature):
            print(f"{creature.transform()}")
            print(f"{creature.attack()}")
            print(f"{creature.revert()}")
        else:
            raise Exception(f"Battle error, aborting tournament: "
                            f"Invalid Creature '{type(creature).__name__}' "
                            f"for this aggressive strategy")

    def is_valid(self, creature: typing.    Any) -> bool:
        try:
            creature.transform
            creature.attack
            creature.revert
            return True
        except AttributeError:
            return False


# Creature with healing capabilities-------------
class DefensiveStrategy(BattleStrategy):
    def act(self, creature: typing. Any) -> None:
        if self.is_valid(creature):
            print(f"{creature.attack()}")
            print(f"{creature.heal()}")
        else:
            raise Exception(f"Battle error, aborting tournament: "
                            f"Invalid Creature '{type(creature).__name__}' "
                            f"for this aggressive strategy")

    def is_valid(self, creature: typing.Any) -> bool:
        try:
            creature.attack
            creature.heal
            return True
        except AttributeError:
            return False
