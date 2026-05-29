#!/usr/bin/env python3
from .ft_creature import Flameling, Pyrodon, Aquabub, Torragon
from abc import ABC, abstractmethod
import typing

'''Abstract class CreatureFactory'''

class CreatureFactory(ABC):
    @abstractmethod
    def create_base():
        pass
    
    @abstractmethod
    def create_evolved():
        pass
    
'''Children class of CreatureFactory'''

class FlameFactory(CreatureFactory):
    def create_base() -> CreatureFactory:
        return Flameling()
    
    def create_evolved() -> CreatureFactory:
        return Pyrodon()

class AquaFactory(CreatureFactory):
    def create_base() -> CreatureFactory:
        return Aquabub()
    
    def create_evolved() -> CreatureFactory:
        return Torragon()