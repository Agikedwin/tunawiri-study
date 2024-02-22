from pydantic import BaseModel, Field
import uuid

class MentalHealthAntenatalModel(BaseModel):
     #id: object = Field(default_factory=uuid.uuid4, alias='_id')
     mchNumber: str
     weeks_pregnant: str
     monthsFirstPregnacyAntentalCare: str
