#!/usr/bin/env python3
from collections.abc import Callable

# -----------------------------------------------
# Grimoire functions for use
# -----------------------------------------------

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def fireball(target: str, power: int) -> str:
    return f"Fireball to {target} for {power} HP"

def power_check(target: str, power: int) -> bool:
    if power > 30 and target:
        return True
    else:
        return False


# -----------------------------------------------
# Spell functions for use
# -----------------------------------------------

def spell1(target: str, power: int) -> str:
    return f"Spell1 to {target} for {power} HP"

def spell2(target: str, power: int) -> str:
    return f"Spell2 to {target} for {power} HP"

def spell3(target: str, power: int) -> str:
    return f"Spell3 to {target} for {power} HP"

def spell4(target: str, power: int) -> str:
    return f"Spell4 to {target} for {power} HP"

def spell5(target: str, power: int) -> str:
    return f"Spell5 to {target} for {power} HP"


# -----------------------------------------------
# Spell-crafting functions system
# -----------------------------------------------

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return (lambda tg, pw: (spell1(tg, pw), spell2(tg, pw)))

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return (lambda tg, pw: (base_spell(tg, pw * multiplier)))

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return (lambda tg, pw: spell(tg, pw) if condition(tg, pw) else "Spell fizzled")

def spell_sequence(spells: list[Callable]) -> Callable:
    return list(map(lambda x: lambda tg, pw: x(tg, pw), spells))


if __name__ == "__main__":
    # Test spell_combiner
    heal_fireball = spell_combiner(fireball, heal)
    print(heal_fireball('The Leader', 80))
    print()

    # Test power_amplifier
    heal_castle = power_amplifier(heal, 4)
    print(heal_castle('Castle', 30))
    print()

    # Test conditional_caster
    fireball_power = conditional_caster(power_check, fireball)
    print(fireball_power('Tower', 20))
    print()

    # Test spell_sequence
    spell_list: list[Callable] = [spell1, spell2, spell3, spell4, spell5]
    spells = spell_sequence(spell_list)
    for spell in spells:
        print(spell('Building', 90))
    
    