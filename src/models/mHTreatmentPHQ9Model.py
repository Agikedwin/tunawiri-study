from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class MentalHealthPHQ9Model(BaseModel):

    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    interest_pleasure: str
    feeling_depressed:str
    trouble_sleeping: str
    feeling_tired: str
    poor_appetite: str
    feeling_bad_about_yourself: str
    trouble_concentrating: str
    slow_or_restless: str
    thoughts_of_harming_yourself: str
    user_id: object
    phq9_score: float
    phq2_score: float | None = 0.0
    severity: str
    color: str
    created_at: datetime = datetime.now()
    comment: str | None = None
    timepoint:  str | None = None
