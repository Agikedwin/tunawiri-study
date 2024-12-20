from datetime import datetime
from typing import Optional

from pydantic import BaseModel,Field
import uuid
class CaseReviewFollowupModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    timepoint: Optional[str] | None = None
    planned_interventions: Optional[str] | None = None
    refferal_to_specialist: Optional[str] | None = None
    crisis_plan: Optional[str] | None = None
    additional_support: Optional[str] | None = None
    review_observation: Optional[str] | None = None
    collaborative_decisions: Optional[str] | None = None
    further_monitoring: Optional[str] | None = None
    comment: Optional[str] | None = None