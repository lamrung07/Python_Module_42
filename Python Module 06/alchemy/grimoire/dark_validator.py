#!/usr/bin/env python3
from .dark_spellbook import dark_spell_allowed_ingredients
# import alchemy.grimoire.dark_spellbook as spellbook


def validate_ingredients(ingredients: str) -> str:
    validated = False
    my_ingredients = ingredients.lower().split(' ')
    allow_ingredients: list[str] = []
    for ingredient in dark_spell_allowed_ingredients():
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
