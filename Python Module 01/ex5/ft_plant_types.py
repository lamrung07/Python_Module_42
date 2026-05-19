#!/usr/bin/env python3
class Plant_Secured:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    def grow(self):
        self._height += 1.2
        self._height = round(self._height, 2)

    def age(self):
        self._age += 1

    def set_height(self, height : float)->None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative\nHeight update rejected")
        else:
            self._height = height
            print(f"Height updated: {height} cm")

    def set_age(self, age : int)->None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative\nAge update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self):
        print(f"{self._name}: {self._height} cm, {self._age} days old")

class Flower(Plant_Secured):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._bloom = 0

    def bloom(self):
        print("[asking the rose to bloom]")
        self._bloom = 1

    def show(self):
        super().show()
        print(f"Color : {self._color}")
        if self._bloom == 0:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")

class Tree(Plant_Secured):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._shade = 0

    def produce_shade(self):
        print("[asking the oak to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

class Vegetable(Plant_Secured):
    def __init__(self, name: str, height: float, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self):
        super().grow()

    def age(self):
        super().age()
        self._nutritional_value += 1

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()

    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
