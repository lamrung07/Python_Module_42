#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory

if __name__ == "__main__":

    # Heal_Factory initialize--------------------
    Heal_Factory = HealingCreatureFactory()
    Sproutling = Heal_Factory.create_base()
    Bloomelle = Heal_Factory.create_evolved()

    # Trans_Factory initialize-------------------
    Trans_Factory = TransformCreatureFactory()
    Shiftling = Trans_Factory.create_base()
    Morphagon = Trans_Factory.create_evolved()

    # Test healing capability--------------------
    print("Testing Creature with healing capability")
    print("base:")
    base_target = "itself"
    print(f"{Sproutling.describe()}")
    print(f"{Sproutling.attack()}")
    print(f"{Sproutling.heal(base_target)}")
    print("evolved:")
    envolved_target = "itself and others"
    print(f"{Bloomelle.describe()}")
    print(f"{Bloomelle.attack()}")
    print(f"{Bloomelle.heal(envolved_target)}")
    print()

    # Test transform capability------------------
    print("Testing Creature with transform capability")
    print("base:")
    print(f"{Shiftling.describe()}")
    print(f"{Shiftling.attack()}")
    print(f"{Shiftling.transform()}")
    print(f"{Shiftling.attack()}")
    print(f"{Shiftling.revert()}")
    print("evolved:")
    print(f"{Morphagon.describe()}")
    print(f"{Morphagon.attack()}")
    print(f"{Morphagon.transform()}")
    print(f"{Morphagon.attack()}")
    print(f"{Morphagon.revert()}")
