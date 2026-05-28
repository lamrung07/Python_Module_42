#!/usr/bin/env python3
from abc import ABC, abstractmethod
import typing
from .ft_creature import Creature

'''Capabilities abstract classes'''

class HealCapability(ABC):
    @abstractmethod
    def heal(self, target) -> str:
        pass
    
class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
    
'''Capabilities concrete classes'''

class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")
        
    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"
    
    def heal(self, target) -> str:
        return f"{self.name} heals {target} for a small amount"
            

class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")
        
    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"
    
    def heal(self, target) -> str:
        return f"{self.name} heals {target} for a large amount"

class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.transformed = 0
        
    def attack(self) -> str:
        if self.transformed == 0:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"
            
    def transform(self) -> str:
        self.transformed = 1
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        return f"{self.name} returns to normal."
    

class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.transformed = 0
        
    def attack(self) -> str:
        if self.transformed == 0:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"
            
    def transform(self) -> str:
        self.transformed = 1
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        return f"{self.name} stabilizes its form."