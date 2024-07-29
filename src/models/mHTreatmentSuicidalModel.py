from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class MentalHealthSuicidalModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    wished_dead_or_to_sleep: str
    thoughts_about_killing_yourself: str
    thinking_about_how_to_kill_Yourself: str
    thoughtsWithIntentionOfActing: str
    worked_out_details_of_killing_yourself: str
    done_anything_to_end_your_life_3month: str
    done_anything_to_end_your_life_lifetime: str
    suicidality_screener_score: str
    suicidal_score: float
    severity: str
    color: str
    created_at: datetime = datetime.now()
    comment: str | None = None
    timepoint: str | None = None

