from pydantic import BaseModel, Field
import uuid


class MentalHealthAntenatalModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    study_id: object
    weeks_pregnant: str
    feelings_when_found_out_pregnant: str
    intentions_with_pregnancy: str
    know_due_date: str
    due_date: str
    months_into_pregnancy_when_first_antental_care: str
    number_of_antental_care_visits: str
