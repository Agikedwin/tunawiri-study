from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class GeneralTreatmentModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    pregnancy_count: int
    created_at: datetime = datetime.now()
    comment: str | None = None
    timepoint:  str | None = None
