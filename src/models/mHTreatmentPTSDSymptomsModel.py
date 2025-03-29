from datetime import datetime

from pydantic import BaseModel, Field
import uuid


class MentalHealthPTSDSymptomsModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    thoughts_memories: str | None = None
    feeling_as_though_event_happening_again: str | None = None
    recurrent_nightmares: str | None = None
    feeling_detached_withdrawn: str | None = None
    unable_to_feel_emotions: str | None = None
    feeling_jumpy_easily_startled: str | None = None
    difficulty_concentrating: str | None = None
    trouble_sleeping: str | None = None
    feeling_on_guard: str | None = None
    feeling_irritable_or_angry: str | None = None
    avoiding_activities_remind_of_event: str | None = None
    less_interest_in_daily_activities: str | None = None
    feeling_no_future: str | None = None
    sudden_emotional_physical_reaction: str | None = None
    avoiding_thoughts_feelings_associated_with_event: str | None = None
    feeling_world_is_dangerous_place: str | None = None
    feeling_you_are_bad_person: str | None = None
    blaming_yourself_for_traumatic_event: str | None = None
    strong_feeling_of_fear_horror_anger_guilt_shame: str | None = None
    difficulty_feeling_love_or_happiness: str | None = None
    taking_risks_that_may_harm_yourself_or_others: str| None = None
    feeling_damaged_by_traumatic_vent: str | None = None
    feeling_something_reminds_you_of_trauma_like_a_dream: str | None = None
    feeling_people_or_objects_around_you_are_strange_or_not_real: str | None = None
    # havard_score holds ptsd5_score front end label data
    havard_score: float | None = 0.0
    severity: str | None = None
    color: str | None = None
    created_at: datetime = datetime.now()
    comment: str | None = None
    timepoint:  str | None = None

    #new fields
    had_nightmares_or_intrusive_thoughts: str | None = None
    traumatic_events: str | None = None
    tried_to_avoid_thoughts_or_situations:str | None = None
    constantly_on_guard_or_easily_startled: str | None = None
    felt_numb_or_detached: str | None = None
    felt_guilty_or_blamed_yourself_or_others: str | None = None
    ptsd5_score: float | None = 0.0

