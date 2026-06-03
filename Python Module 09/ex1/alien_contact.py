#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator
from enum import Enum
from typing import Optional, List, Any
from datetime import datetime, timezone

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)
    
    
    @model_validator(mode='after')
    def validator(self):
        if self.contact_id[0] != 'A' or self.contact_id[1] != 'C':
            raise ValueError ("Contact ID must start with 'AC'")
        if not self.is_verified:
            raise ValueError ("Physical contact reports must be verified")
        if 
        
        
        