import uuid
from typing import Optional
from pydantic import BaseModel, Field, validator

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
    user_id : object
    cd4_count_known: str
    cd4_count_unknown: str
    known_cd4_count: str
    cd4_count_date: str
    viral_load_known: str
    viral_load_unknown: str
    known_viral_load: str
    viral_load_date: str
    art_start_date: str
    current_art_regimen: str
    last_hiv_visit_date: str
    missed_visits_no: str
    missed_visits_yes: str
    missed_visits_count: str