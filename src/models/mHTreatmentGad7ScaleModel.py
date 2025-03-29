from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class MentalHealthGad7ScaleModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    feeling_nervous_anxious: str
    not_able_to_stop_worrying: str
    worrying_too_much: str
    trouble_relaxing: str
    restless_difficulty_sitting_still: str
    easily_annoyed_irritable: str
    feeling_afraid_something_awful_might_happen: str
    user_id: object
    gad7_score: float
    severity: str
    color: str
    gad2_score:  float | None = 0.0
    created_at: datetime = datetime.now()
    comment: str | None = None
    timepoint:  str | None = None
