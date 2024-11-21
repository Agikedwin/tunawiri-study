import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator


class VLgraphModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    known_viral_load: str
    viral_load_date: str
    user_id: object

class PHQ9Model(BaseModel):
    phg9_id: object = Field(default_factory=uuid.uuid4, alias='_id')
    phq9_score: Optional[object] = 0.0
    created_at: str

class Gad7Model(BaseModel):
    gad_id: object = Field(default_factory=uuid.uuid4, alias='_id')
    gad7_score: Optional[object] = 0.0
    created_at: str

class Phq9Gad7(PHQ9Model):
    gad7: Gad7Model
