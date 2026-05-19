#!/usr/bin/env python3
class Plant_Secured:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._stats = self.Stats(self)
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    @staticmethod
    def age_check(plant_age):
        if plant_age > 365:
            print(f"Is {plant_age} days more than a year? -> True")
        else:
            print(f"Is {plant_age} days more than a year? -> False")

    @classmethod
    def anonymous(cls):
        return cls(name="Unknown plant", height=0.0, age=0)

    def grow(self):
        self._height += 20
        self._stats._grow_call += 1

    def age(self):
        self._age += 1
        self._stats._age_call += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height} cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self):
        self._stats._show_call += 1
        print(f"{self._name}: {self._height} cm, {self._age} days old")

    class Stats:
        def __init__(self, plant) -> None:
            self._plant = plant
            self._grow_call = 0
            self._age_call = 0
            self._show_call = 0

        def display(self) -> None:
            print(f"[statistics for {self._plant._name}]")
            print(f"Stats: {self._grow_call} grow, {self._age_call} age,")
            print(f" {self._show_call} show")


class Flower(Plant_Secured):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom = 0

    def bloom(self):
        self._bloom = 1

    def show(self):
        super().show()
        print(f"Color : {self._color}")
        if self._bloom == 0:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree(Plant_Secured):
    def __init__(self, name: str, height: float, age: int, trunk: float):
        super().__init__(name, height, age)
        self._trunk = trunk
        self._shade = 0
        self._produce_shade_call = 0

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(f"Tree {self._name}")
        print(f" now produces a shade of {self._height}cm long")
        print(f" and {self._trunk}cm wide.")
        self._produce_shade_call += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk}cm")

    def display(self) -> None:
        self._stats.display()
        print(f"{self._produce_shade_call} shade")


class Vegetable(Plant_Secured):
    def __init__(self, name: str, height: float, age: int, hv_season: str):
        super().__init__(name, height, age)
        self._harvest_season = hv_season
        self._nutritional_value = 0

    def grow(self) -> None:
        super().grow()

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        if self._bloom == 0:
            self._seed = 0
        else:
            self._seed = 42

    def show(self):
        super().show()
        print(f"Seeds: {self._seed}")


def display_stats(plant: Plant_Secured):
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant_Secured.age_check(30)
    Plant_Secured.age_check(400)

    print("\n=== Flower")
    Rose = Flower("Rose", 15.0, 10, "red")
    Rose.show()
    display_stats(Rose)
    print("[asking the rose to grow and bloom]")
    Rose.grow()
    Rose.bloom()
    Rose.show()
    display_stats(Rose)

    print("\n=== Tree")
    Oak = Tree("Oak", 200.0, 365, 5.0)
    Oak.show()
    Oak.display()
    Oak.produce_shade()
    Oak.display()

    print("\n=== Seed")
    Sunflower = Seed("Sunflower", 80, 45, "yellow")
    Sunflower.show()
    print("[make sunflower grow, age and bloom]")
    for i in range(1, 10):
        Sunflower.age()
        Sunflower.grow()
    Sunflower.bloom()
    Sunflower.show()
    Sunflower._stats.display()

    print("\n=== Anonymous")
    Anonymous = Plant_Secured.anonymous()
    Anonymous.show()
    Anonymous._stats.display()
