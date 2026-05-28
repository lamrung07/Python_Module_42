#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory

def ft_test_factory(factory) -> None:
    print("Testing factory")
    print(f"{factory.create_base().describe()}")
    print(f"{factory.create_base().attack()}")
    print(f"{factory.create_evolved().describe()}")
    print(f"{factory.create_evolved().attack()}")
    print()

def ft_test_battle(factory1, factory2) -> None:
    print("Testing battle")
    print(f"{factory1.create_base().describe()}")
    print("vs.")
    print(f"{factory2.create_base().describe()}")
    print("fight!")
    print(f"{factory1.create_base().attack()}")
    print(f"{factory2.create_base().attack()}")
    

if __name__ == "__main__":
    #-------Test factory-----#
    ft_test_factory(FlameFactory)
    ft_test_factory(AquaFactory)
    
    #-------Test battle------#
    ft_test_battle(FlameFactory, AquaFactory)