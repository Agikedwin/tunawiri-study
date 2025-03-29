from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class ArtAdherenceModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    missed_doses: str
    medicines_taking_quality: str
    medicine_frequency: str
    art_score: float | None = 0.0
    created_at: datetime = datetime.now()
