#!/usr/bin/env python3
from abc import ABC, abstractmethod
import typing

'''Abstract class Creature()'''

class Creature(ABC):
    def __init__(self, name, creature_type):
        self.name = name
        self.type = creature_type

    @abstractmethod
    def attack(self) -> None:
        pass
    
    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


'''Children classes of Creature()'''

class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self):
        return f"{self.name} uses Ember!"

class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self):
        return f"{self.name} uses Flamethrower!"

class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self):
        return f"{self.name} uses Water Gun!"

class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self):
        return f"{self.name} uses Hydro Pump!"

