from pydantic import BaseModel, Field
import uuid


class MentalHealthPostnatalModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    pregnancy_end_duration: str
    pregnancy_end_method: str
    place_of_birth: str
    otherPlaceOfBirth: str
    birth_complications: str
    infant_alive: str
    infant_passing_age: str
    weeks_of_pregnancy_at_birth: str
    birth_weight: str
    infant_feeding_option: str
    breastfeeding_status: str
    vaccinations_received: str
    HIV_test_done: str
    HIV_test_timing: str
    HIV_status: str
    enrolled_at_HIV_clinic: str
    ARV_course_completed: str
    purpose_of_ARV_drugs: str
