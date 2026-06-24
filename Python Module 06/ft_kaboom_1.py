#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        print(f"Testing record dark spell: "
              f"{dark_spell_record('Evil', 'Bats, frogs and eyeball')}")
    except ImportError as e:
        print(f"ERROR : {e}")
