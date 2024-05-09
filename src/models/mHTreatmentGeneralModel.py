from pydantic import BaseModel, Field
import uuid


class GeneralTreatmentModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    pregnancy_count: int
