import uuid
from typing import Optional
from pydantic import BaseModel, Field, validator
from datetime import datetime


class VitalsModel(BaseModel):
    bloodPressure: str
    weight: float
    height: float
    bmi: float

class CD4CountModel(BaseModel):
    cd4CountKnown: Optional[str] | None = None
    cd4CountUnknown: Optional[str]
    knownCd4Count: Optional[str]
    cd4CountDate: Optional[str]

class ViralLoad(BaseModel):
    viralLoadKnown: Optional[str]
    viralLoadUnknown: Optional[str]
    knownViralLoad: Optional[str]
    viralLoadDate: Optional[str]


class ClinicalModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    art_start_date: str
    cd4_count_date: str
    cd4_known: str
    current_art_regimen: str
    ever_missed_visit: str
    known_cd4_count: str
    known_viral_load: str
    art_start_date: str
    current_art_regimen: str
    last_hiv_visit_date: str
    other_regimen_name: str
    viral_load_date: str
    viral_load_known: str
    scheduled_visit_date: Optional[str] = None
    actual_visit_date: Optional[str] = None
    missed_visits_count: Optional[str] = None
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True
