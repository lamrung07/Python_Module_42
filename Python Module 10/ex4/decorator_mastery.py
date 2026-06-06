#!/usr/bin/env python3
import time
import functools
from typing import Callable


# ─────────────────────────────────────────────
# 1. spell_timer
# ─────────────────────────────────────────────
def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


# ─────────────────────────────────────────────
# 2. power_validator
# ─────────────────────────────────────────────
def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # power is the second positional arg after self: args[2]
            # or first positional arg for standalone: args[1]
            power = None
            if "power" in kwargs:
                power = kwargs["power"]
            elif len(args) >= 3:
                power = args[2]   # (self, spell_name, power)
            elif len(args) >= 2:
                power = args[1]   # (spell_name, power) standalone

            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


# ─────────────────────────────────────────────
# 3. retry_spell
# ─────────────────────────────────────────────
def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


# ─────────────────────────────────────────────
# 4. MageGuild
# ─────────────────────────────────────────────
class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


# ─────────────────────────────────────────────
# Demo — matches expected output exactly
# ─────────────────────────────────────────────
if __name__ == "__main__":

    # ── spell_timer ──────────────────────────
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    # ── retry_spell ──────────────────────────
    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def waaaaaaagh() -> str:
        raise RuntimeError("fizzle")

    result = waaaaaaagh()
    print(result)
    print("Waaaaaaagh spelled !")

    # ── MageGuild ────────────────────────────
    print("\nTesting MageGuild...")

    print(MageGuild.validate_mage_name("Merlin"))   # True
    print(MageGuild.validate_mage_name("X1"))        # False

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))         # valid power
    print(guild.cast_spell("Spark", 5))              # invalid power