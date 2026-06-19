#!/usr/bin/env python3
# from .dark_validator import validate_ingredients
import alchemy.grimoire.dark_validator as validator


def dark_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ['bats', 'frogs', 'arsenic', 'eyeball']
    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validate_message = validator.validate_ingredients(ingredients)
    if validate_message.find('INVALID'):
        return f" Spell rejected: {spell_name} ({validate_message})"
    if validate_message.find('VALID'):
        return f" Spell recorded: {spell_name} ({validate_message})"
    return "Ingredients were not validated"
