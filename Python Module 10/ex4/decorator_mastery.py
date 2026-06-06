#!/usr/bin/env python3
import time
from typing import Callable
from functools import wraps

def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:
    pass

def retry_spell(max_attempts: int) -> Callable:
    pass

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass
    def cast_spell(self, spell_name: str, power: int) -> str:
        pass