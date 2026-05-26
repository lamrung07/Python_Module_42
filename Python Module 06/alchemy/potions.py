#!/usr/bin/env python3
from .elements import create_air, create_earth
from elements import create_fire, create_water
def healing_potion():
    return_message = (f"Healing potion brewed with '{create_earth()}' "
                    f"and '{create_air()}'")
    return return_message
            
def strength_potion():
    return_message = (f"Strength potion brewed with ’{create_fire()}’ "
                    f"and '{create_water()}'")
    return return_message
            