#!/usr/bin/env python3
from .ft_capabilities import Sproutling, Bloomelle, Shiftling, Morphagon


'''Capabilities factory classes'''


class HealingCreatureFactory():
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory():
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
