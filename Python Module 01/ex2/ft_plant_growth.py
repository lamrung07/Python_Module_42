#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        self.height += 1.2
        self.height = round(self.height, 2)

    def age(self) -> None:
        self.plant_age += 1
        
    def show(self) -> None:
        print(f"{self.name}: {self.height} cm, {self.plant_age} days old")
		
def simulate_week(plant : Plant) -> None:
    print("=== Garden Plant Growth ===")
    plant.show()
    start_height = plant.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()
    growth = round(plant.height - start_height, 2)
    print(f"Growth this week: {growth}cm")

if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    simulate_week(rose)
        
