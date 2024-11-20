from datetime import datetime
from pydantic import BaseModel,Field
import uuid

class CaseReviewInitialModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    timepoint: str
    anxietycategorization: str
    depressioncategorization: str
    anxiety_score: str
    Phq9_score: str
    takingMedications: str
    dosage: str
    changeInDosage: str
    duration: str
    adherence: str
    side_effect: str
    alternative_treatment: str
    current_therapy: str
    other_current_therapy: str
    receiving_pm: str
    no_pm_sessions: str
    recent_psychlops: str
    frequency_of_therapy: str
    other_therapy_frequency: str
    engagement_therapy: str
    treatment_goals: str
    coping_strategies: str
    phq9ActualScore: str
    anxietyActualScore: str
    patient_satisfaction: str
    comment: str
