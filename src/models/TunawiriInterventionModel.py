from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class TunawiriInterventionModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    timepoint: str
    involved_in_tunawiri: str
    sessions_attended: str
    session_leader: str
    othersession_leader: str
    average_meeting_length: str
    still_involved: str
    program_helpfulness: str
    created_at: datetime = datetime.now()
    comment: str | None = None
    timepoint:  str | None = None
