#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    try:
        MySpaceStation = SpaceStation(
                            station_id='2004',
                            name='MyTyson',
                            crew_size=90,
                            power_level=40.9,
                            oxygen_level=30.23,
                            last_maintenance=datetime.now(),
                            is_operational='hello',
                            notes="Operational"
                        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg']} (field: {error['loc'][0]})")
        return
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    print(f"ID: {MySpaceStation.station_id}")
    print(f"Name: {MySpaceStation.name}")
    print(f"Crew: {MySpaceStation.crew_size} people")
    print(f"Power: {MySpaceStation.power_level}%")
    print(f"Oxygen: {MySpaceStation.oxygen_level}%")
    print(f"Status: {MySpaceStation.is_operational}")
    print("\n========================================")


if __name__ == "__main__":
    main()
