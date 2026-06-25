#!/usr/bin/env python3
from .ft_capabilities import Sproutling, Bloomelle, Shiftling, Morphagon
from .ft_creature_factory import CreatureFactory

'''Capabilities factory classes'''


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
