#!/usr/bin/env python3
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any

'''Base enchantment function'''
def enchant(power: int, element: str, target: str) -> str:
        return f"Enchanting '{target}' with {element} at power {power}!"


'''Requirement functions'''
def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == 'add':
        return reduce(lambda x,y: add(x, y), spells)
    elif operation == 'multiply':
        return reduce(lambda x,y: mul(x, y), spells)
    elif operation == 'max':
        return max(spells)
    elif operation == 'min':
        return min(spells)
    else:
        raise ValueError("Unknown Operation. Please try again!")

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    version1 = partial(base_enchantment, power=50, element='Water')
    version2 = partial(base_enchantment, power=50, element='Fire')
    version3 = partial(base_enchantment, power=50, element='Wind')
    return {
        'Water': version1,
        'Fire': version2,
        'Wind': version3
    }

@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def print_type(spell: Any, type: str) -> None:
        return "Unknown spell type"
    
    @print_type.register(int)
    def _(spell, type):
        return f"{type}: {spell} damage"
    
    @print_type.register(str)
    def _(spell, type):
        return f"{type}: {spell}"
    
    @print_type.register(list)
    def _(spell, type):
        return f"{type}: {len(spell)} spells"

    return print_type

if __name__ == "__main__":
    '''Testing spell reducer'''
    print("Testing spell reducer...")
    production = [10, 30, 40, 25, 50]
    try:
        print(f"Sum: {spell_reducer(production, 'add')}")
        print(f"Product: {spell_reducer(production, 'multiply')}")
        print(f"Max: {spell_reducer(production, 'max')}")
        print(f"Min: {spell_reducer(production, 'min')}")
    except ValueError as e:
        print(f"{e}")
    print()
    
    '''Testing partial enchanter'''
    print("Testing partial enchanter...")
    Enchanters = partial_enchanter(enchant)
    for name, spell in Enchanters.items():
        print(f"   {name}: {spell(target='sword')}")
    
    '''Test memoized fibonacci'''
    print("Test memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())
    print()
    
    '''Testing spell dispatcher'''
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"{dispatcher(42, 'Damage spell')}")
    print(f"{dispatcher('fireball', 'Enchantment')}")
    spells = ['Fire', 'Heal', 'Destroy']
    print(f"{dispatcher(spells, 'Multi-cast')}")
    print(f"{dispatcher({'Unknown' : 'Unknown'}, 'Unknown-type')}")
