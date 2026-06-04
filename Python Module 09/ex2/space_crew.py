#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from typing import Optional, List, Any
from datetime import datetime

class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)

'''Helper functions for validation rules'''

def Crew_validator(crew: List[CrewMember]) -> bool:
    for Member in crew:
        if Member.rank.value == 'commander' or Member.rank.value == 'captain':
            return True
    return False

def Long_mission_validator(duration: int, crew: List[CrewMember]) -> bool:
    crew_num = len(crew)
    count = 0
    if duration > 365:
        for Member in crew:
            if Member.years_experience >= 5:
                count += 1
        experienced = round(count/crew_num, 2)
        return experienced > 0.5
    return True

        
'''Space Mission'''
class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember]
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)
    
    @model_validator(mode='after')
    def validator(self):
        if self.mission_id[0] != 'M':
            raise ValueError('Mission ID must start with "M"')
        if not Crew_validator(self.crew):
            raise ValueError("Must have at least one Commander or Captain")
        if not Long_mission_validator(self.duration_days, self.crew):
            raise ValueError("Long missions (> 365 days) need 50 percent experienced crew (5+ years)")
        for Member in self.crew:
            if Member.is_active == False:
                raise ValueError("All crew members must be active")
        return self
            
def main():
    try:
        #-------Crew Members-------------------#
        Sarah_Connor = CrewMember(
                    member_id='MA_124',
                    name='Sarah Connor',
                    rank='commander',
                    age=33,
                    specialization='Mission Command',
                    years_experience=10,
                    is_active=True
                )
        John_Smith = CrewMember(
                    member_id='MJ_537',
                    name='John Smith',
                    rank='lieutenant',
                    age=45,
                    specialization='Navigation',
                    years_experience=3,
                    is_active=True
                )
        Alice_Johnson = CrewMember(
                    member_id='ML_112',
                    name='Alice_Johnson',
                    rank='officer',
                    age=44,
                    specialization='Engineering',
                    years_experience=7,
                    is_active=True
                )
        
        #-------------Mission-----------------------#
        Mars_Colony = SpaceMission(
                    mission_id='M2024_MARS',
                    mission_name='Mars Colony Establishment',
                    destination='Mars',
                    launch_date=datetime(2026, 6, 4, 14, 30, 0),
                    duration_days=900,
                    crew=[Sarah_Connor, John_Smith, Alice_Johnson],
                    budget_millions=2500.0
                )
    except ValidationError as e:
        print ("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg']}")
        return
    
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {Mars_Colony.mission_name}")
    print(f"ID: {Mars_Colony.mission_id}")
    print(f"Destination: {Mars_Colony.destination}")
    print(f"Duration: {Mars_Colony.duration_days} days")
    print(f"Budget: ${Mars_Colony.budget_millions}M")
    print(f"Crew size: {len(Mars_Colony.crew)}")
    print("Crew members:")
    for Crew in Mars_Colony.crew:
        print(f"- {Crew.name} ({Crew.rank.value}) - {Crew.specialization}")
    print()
    print("No validation errors found")
    print("=========================================")


if __name__ == "__main__":
    main()