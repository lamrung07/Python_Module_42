#!/usr/bin/env python3
# from .light_spellbook import light_spell_allowed_ingredients
import alchemy.grimoire.light_spellbook as spellbook
"""Indirectly import from parent module to avoid dependencies"""


def validate_ingredients(ingredients: str) -> str:
    validated = False
    my_ingredients = ingredients.lower().split(' ')
    allow_ingredients: list[str] = []
    for ingredient in spellbook.light_spell_allowed_ingredients():
        allow_ingredients.append(ingredient.lower())
    for my_ingredient in my_ingredients:
        if my_ingredient in allow_ingredients:
            validated = True
            break
    return_str = ''
    if validated:
        return_str += ingredients + ' - VALID'
    else:
        return_str += ingredients + ' - INVALID'
    return return_str
