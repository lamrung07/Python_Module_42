#!/usr/bin/env python3
from .light_validator import validate_ingredients
import alchemy.grimoire.light_validator as validator


def light_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ['earth', 'air', 'fire', 'water']
    return ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validate_message = validator.validate_ingredients(ingredients)
    if validate_message.find('INVALID'):
        return f" Spell rejected: {spell_name} ({validate_message})"
    if validate_message.find('VALID'):
        return f" Spell recorded: {spell_name} ({validate_message})"
    return "Ingredients were not validated"
