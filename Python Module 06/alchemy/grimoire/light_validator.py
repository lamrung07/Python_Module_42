#!/usr/bin/env python3
from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    validated = False
    my_ingredients = ingredients.lower().split(' ')
    allow_ingredients = light_spell_allowed_ingredients().lower()
    for my_ingredient in my_ingredients:
        if my_ingredient in allow_ingredients:
            validated = True
            break
    return_str = ''
    if validated:
        return_str += ingredients + '- VALID'
    else:
        return_str += ingredients + '- INVALID'
    return return_str
        
    
    
    