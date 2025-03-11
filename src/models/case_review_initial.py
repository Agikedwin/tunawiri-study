from datetime import datetime
from typing import Optional

from pydantic import BaseModel,Field
import uuid

class CaseReviewInitialModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    anxietycategorization: Optional[str]| None = None
    depressioncategorization: Optional[str]| None = None
    anxiety_score: Optional[str]| None = None
    Phq9_score: Optional[str]| None = None
    takingMedications: Optional[str] | None = None
    dosage: Optional[str]| None = None
    changeInDosage: Optional[str] | None = None
    duration: Optional[str] | None = None
    adherence: Optional[str] | None = None
    side_effect: Optional[str]| None = None
    alternative_treatment: Optional[str]| None = None
    current_therapy: Optional[str]| None = None
    other_current_therapy: Optional[str]| None = None
    receiving_pm: Optional[str]| None = None
    no_pm_sessions: Optional[str]| None = None
    recent_psychlops: Optional[str]| None = None
    frequency_of_therapy: Optional[str]| None = None
    other_therapy_frequency: Optional[str]| None = None
    engagement_therapy: Optional[str]| None = None
    treatment_goals: Optional[str]| None = None
    coping_strategies: Optional[str]| None = None
    phq9ActualScore: Optional[str]| None = None
    anxietyActualScore: Optional[str]| None = None
    patient_satisfaction: Optional[str]| None = None

    #followup values
    timepoint: Optional[str] | None = None
    planned_interventions: Optional[str] | None = None
    refferal_to_specialist: Optional[str] | None = None
    crisis_plan: Optional[str] | None = None
    additional_support: Optional[str] | None = None
    review_observation: Optional[str] | None = None
    collaborative_decisions: Optional[str] | None = None
    further_monitoring: Optional[str] | None = None
    comment: Optional[str] | None = None
