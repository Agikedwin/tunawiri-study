from pydantic import BaseModel, Field
import uuid


class MentalHealthPostnatalModel(BaseModel):
    pregnancyEndDuration: str
    placeOfBirth: str
    otherPlaceOfBirth: str
    infantAlive: str
    infantPassingAge: str
    HIVTestDone: str
