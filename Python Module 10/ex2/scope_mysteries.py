#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any

def mage_counter() -> Callable:
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment


def spell_accumulator(initial_power: int) -> Callable:
    accumulation = initial_power
    def accumulator(value: int) -> int:
        nonlocal accumulation
        accumulation += value
        return accumulation
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda x: enchantment_type + ' ' + x


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: Any, value: Any):
        nonlocal storage
        storage[key] = value
        print(f"Store '{key}' = {value}")

    def recall(key: Any):
        nonlocal storage
        return storage.get(key, "Memory not found")
        
    return {'store': store, 'recall': recall}
    
        
        

if __name__ == "__main__":
    
    '''Testing mage counter'''
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_a call 3: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()
    
    '''Testing spell accumulator'''
    print("Testing spell accumulator...")
    result = spell_accumulator(100)
    print(f"Base 100, add 20: {result(20)}")
    print(f"Base 100, add 30: {result(30)}")
    print()
    
    '''Testing enchantment factory'''
    print("Testing enchantment factory...")
    enchantment1 = enchantment_factory('Flaming')
    enchantment2 = enchantment_factory('Frozen')
    print(f"{enchantment1('Sword')}")
    print(f"{enchantment2('Shield')}")
    print()

    '''Testing memory vault'''
    print("Testing memory vault...")
    memory = memory_vault()
    memory["store"]("secret", 42)
    print(f"Recall 'secret': {memory['recall']('secret')}")
    print(f"Recall 'unknown': {memory['recall']('unknown')}")