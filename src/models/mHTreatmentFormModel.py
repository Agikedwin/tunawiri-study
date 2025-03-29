from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class MmTreatmentFormModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    #mental_health_disorder: str
    #community_care: str
    #visit_hospital_clinic: str
    #treatment: str
    #other_treatments: str
    #medicine: str
    #taking_as_prescribed: str


    #new values
    mental_health_treatment:  str | None = None
    sessions_completed:  str | None = None
    session_complete_date:  str | None = None
    recent_psychlops:  str | None = None
    other_therapy:  str | None = None
    telepsychiatry:  str | None = None
    telepsychiatry_date:  str | None = None
    psychiatrist_recommendation:  str | None = None
    psychoactive_medicine:  str | None = None
    psychoactive_medicinetaken:  str | None = None
    medicine:  str | None = None
    taking_as_prescribed:  str | None = None

    user_id: object  | None = None
    created_at: datetime = datetime.now()
    comment: str | None = None
    timepoint:  str | None = None



