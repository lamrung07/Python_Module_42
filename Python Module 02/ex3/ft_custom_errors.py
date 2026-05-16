#!/usr/bin/env python3

class  GardenError(Exception):
	def __init__(self, message="Unknown plant error") -> None:
		super().__init__(message)
		self.message = message
	def __str__(self) -> str:
		return 	f"Caught GardenError: {self.message}"

class	HouseError(GardenError):
	def __init__(self, message) -> None:
		super().__init__(message)
	def __str__(self) -> str:
		return 	f"Caught HouseError: {self.message}"

class	PlantError(GardenError):
	def __init__(self, message) -> None:
		super().__init__(message)
	def __str__(self) -> str:
		return 	f"Caught PlantError: {self.message}"
	
class	WaterError (GardenError):
	def __init__(self, message) -> None:
		super().__init__(message)
	def __str__(self) -> str:
		return 	f"Caught WaterError: {self.message}"

def	raise_planterror(message):
	try:
		raise PlantError(message)
	except PlantError as e:
		print(f"{e}\n")

def	raise_watererror(message):
	try:
		raise WaterError(message)
	except WaterError as e:
		print(f"{e}\n")

def raise_gardenerror(errors):
	errors = [
        PlantError(message),
        WaterError(message),
        HouseError(message),
    ]
	for error in errors:
		try:
			raise PlantError(message)
			raise WaterError(message)
			raise HouseError(message)
		except GardenError as e:
			print(GardenError.__str__(e))

if __name__ == "__main__":
	print("=== Custom Garden Errors Demo ===\n")

	print("Testing PlantError...")
	raise_planterror("The tomato plant is wilting!")

	print("Testing WaterError...")
	raise_watererror("Not enough water in the tank!")

	print("Testing catching all garden errors...")
	errors = [
		PlantError("The tomato plant is wilting!"),
		WaterError("Not enough water in the tank!"),
		HouseError("My House is cold")
	]
	raise_gardenerror(errors)
	print("All custom error types work correctly!")