#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from typing import Optional, List, Any
from datetime import datetime, timezone


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"
    

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)
    
    
    @model_validator(mode='after')
    def validator(self):
        if self.contact_id[0] != 'A' or self.contact_id[1] != 'C':
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type.name == "PHYSICAL":
            if not self.is_verified:
                raise ValueError("Physical contact reports must be verified")
        if self.contact_type.name == "TELEPATHIC":
            if self.witness_count < 3:
                raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received == None:
            raise ValueError(" Strong signals (> 7.0) should include received messages")
        return self


def main():
    try:
        MarsContact = AlienContact(
                        contact_id='AC_2024_001',
                        timestamp=datetime(2022, 7, 4, 14, 30, 0),
                        location='Area 51, Nevada',
                        contact_type='physical',
                        signal_strength=8.5,
                        duration_minutes=45,
                        witness_count=5,
                        message_received='Greetings from Zeta Reticuli',
                        is_verified=False
                    )
    except ValidationError as e:
        print ("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg']} (field: {error['loc'][0]})")
        return

    print("Alien Contact Log Validation")
    print("========================================")
    print(f"Valid contact report:")
    print(f"ID: {MarsContact.contact_id}")
    print(f"Timestamp: {MarsContact.timestamp}")
    print(f"Type: {MarsContact.contact_type.value}")
    print(f"Location: {MarsContact.location}")
    print(f"Signal: {MarsContact.signal_strength}/10")
    print(f"Duration: {MarsContact.duration_minutes} minutes")
    print(f"Witnesses: {MarsContact.witness_count}")
    print(f"Message: {MarsContact.message_received}")
    print("\n========================================")
        
        
if __name__ == "__main__":
    main()