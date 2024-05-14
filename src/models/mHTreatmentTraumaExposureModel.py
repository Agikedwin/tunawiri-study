from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class MentalHealthTraumaExposureModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    witnessed_murder_of_family_or_friend: str
    witnessed_murder_of_stranger_or_known_person: str
    witnessed_armed_attack_on_someone: str
    left_country_due_to_war_conflict_poverty: str
    sexually_assaulted_or_raped: str
    experienced_torture: str
    robbed_at_gun_point_or_knife_point: str
    kidnapped: str
    felt_close_to_death: str
    witnessed_someone_being_raped: str
    trauma_score: float
    severity: str
    color: str
    created_at: datetime = datetime.now()
