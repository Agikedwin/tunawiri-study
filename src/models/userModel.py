import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator


class User(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    mch_number: str
    first_name: str
    other_names: str
    dob: str
    marital_status: str
    education_level: str
    reading_ability: str
    religion: str
    home_language: str
    study_id: str
    created_at: datetime = datetime.now()