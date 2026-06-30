#!/usr/bin/env python3
from .ft_creature import Flameling, Pyrodon, Aquabub, Torragon
from .ft_creature import Creature
from abc import ABC, abstractmethod


'''Abstract class CreatureFactory'''


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass


'''Children class of CreatureFactory'''


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
