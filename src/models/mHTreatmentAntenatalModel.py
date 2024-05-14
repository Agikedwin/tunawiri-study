from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class MentalHealthAntenatalModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    gestational_age_weeks: str
    months_pregnancy_antenatal_care: str
    created_at: datetime = datetime.now()
