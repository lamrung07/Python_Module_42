#!/usr/bin/env python3
from .ft_capabilities import Sproutling, Bloomelle, Shiftling, Morphagon

'''Capabilities factory classes'''
class HealingCreatureFactory():
    def create_base() -> None:
        return Sproutling()
    
    def create_evolved() -> None:
        return Bloomelle()

class TransformCreatureFactory():
    def create_base() -> None:
        return Shiftling()
    
    def create_evolved() -> None:
        return Morphagon()