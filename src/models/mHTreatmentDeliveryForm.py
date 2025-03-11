from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class MentalHealthDeliveryFormModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    #gestational_age_weeks: str
    #months_pregnancy_antenatal_care: str
    created_at: datetime = datetime.now()
    comment: str | None = None
    timepoint:  str | None = None

    #new values
    pregnancy_end_duration: str | None = None
    pregnancy_end_method: str | None = None
    place_of_birth: str | None = None
