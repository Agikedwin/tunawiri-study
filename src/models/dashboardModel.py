from typing import Optional
from pydantic import BaseModel, Field, validator

from src.models.clinicalModel import ClinicalModel
from src.models.userModel import User


class Dashboard(BaseModel):
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
    clinical:Optional[ClinicalModel]

