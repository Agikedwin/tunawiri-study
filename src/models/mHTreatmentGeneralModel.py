from pydantic import BaseModel, Field
import uuid

class MentalHealthTreatmentModel(BaseModel):
     #id: object = Field(default_factory=uuid.uuid4, alias='_id')
     mchNumber: str
     pregnancyCount : int
