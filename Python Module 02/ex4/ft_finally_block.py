#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, name) -> None:
        super().__init__(self, name)
        self.name = name

    def __str__(self) -> str:
        return "Caught PlantError: Invalid plant name to water"


def water_plant(plant_name: str):
    if (plant_name[0] == plant_name.capitalize()[0]):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(plant_name)


def test_watering_system(plants):
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"{e}: '{plant}'\n.. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    valid_plants = ['Tomato', 'Lettuce', 'Carrots']
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    test_watering_system(valid_plants)

    invalid_plants = ['Tomato', 'lettuce', 'carrots']
    print("Testing valid plants...")
    test_watering_system(invalid_plants)

    print("Cleanup always happens, even with errors!")
