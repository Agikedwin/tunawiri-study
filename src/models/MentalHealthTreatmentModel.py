from pydantic import BaseModel, Field
import uuid


class MentalHealthTreatmentModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    mental_health_disorder: str
    community_care: str
    visit_hospital_clinic: str
    treatment: str
    other_treatments: str
    medicine: str
    taking_as_prescribed: str
