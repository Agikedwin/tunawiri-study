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
    #id: str = Field(default_factory=uuid.uuid4, alias='_id')
    vitals:VitalsModel | None = None
    cd4Count:CD4CountModel | None = None
    viralLoad: ViralLoad | None = None
    artStartDate: str
    currentArtRegimen: str
    lastHIVVisitDate: str
    missedVisitsNo: str
    missedVisitsYes: str
    missedVisitsCount: int







