from datetime import datetime
from pydantic import BaseModel,Field
import uuid
class CaseReviewFollowupModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    timepoint: str
    planned_interventions: str
    refferal_to_specialist: str
    crisis_plan: str
    additional_support: str
    review_observation: str
    collaborative_decisions: str
    further_monitoring: str
    comment: str