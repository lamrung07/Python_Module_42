#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"Caught GardenError: {self.message}"


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return f"Caught PlantError: {self.message}"


class WaterError (GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return f"Caught WaterError: {self.message}"


def raise_planterror(message) -> None:
    try:
        raise PlantError(message)
    except PlantError as e:
        print(f"{e}")


def raise_watererror(message) -> None:
    try:
        raise WaterError(message)
    except WaterError as e:
        print(f"{e}")


def raise_gardenerror(message) -> None:
    try:
        raise GardenError(message)
    except GardenError as e:
        print(f"{e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    raise_planterror("The tomato plant is wilting!")
    print()
    print("Testing WaterError...")
    raise_watererror("Not enough water in the tank!")
    print()
    print("Testing catching all garden errors...")
    errors = [
        "The tomato plant is wilting!",
        "Not enough water in the tank!",
    ]
    print()
    for error in errors:
        raise_gardenerror(error)
    print("\nAll custom error types work correctly!")
