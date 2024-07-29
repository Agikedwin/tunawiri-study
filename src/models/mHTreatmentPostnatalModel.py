from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class MentalHealthPostnatalModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    pregnancy_end_duration: str
    pregnancy_end_method: str
    place_of_birth: str
    infant_alive: str
    infant_passing_age:str
    created_at: datetime = datetime.now()
    comment: str | None = None
    timepoint:  str | None = None
