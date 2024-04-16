from pydantic import BaseModel, Field
import uuid


class MentalHealthHarvardTraumaModel(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    user_id: object
    thoughts_memories: str
    feeling_as_though_event_happening_again: str
    recurrent_nightmares: str
    feeling_detached_withdrawn: str
    unable_to_feel_emotions: str
    feeling_jumpy_easily_startled: str
    difficulty_concentrating: str
    trouble_sleeping: str
    feeling_on_guard: str
    feeling_irritable_or_angry: str
    avoiding_activities_remind_of_event: str
    less_interest_in_daily_activities: str
    feeling_no_future: str
    sudden_emotional_physical_reaction: str
    avoiding_thoughts_feelings_associated_with_event: str
    feeling_world_is_dangerous_place: str
    feeling_you_are_bad_person: str
    blaming_yourself_for_traumatic_event: str
    strong_feeling_of_fear_horror_anger_guilt_shame: str
    difficulty_feeling_love_or_happiness: str
    taking_risks_that_may_harm_yourself_or_others: str
    feeling_damaged_by_traumatic_vent: str
    feeling_something_reminds_you_of_trauma_like_a_dream: str
    feeling_people_or_objects_around_you_are_strange_or_not_real: str
    harvard_trauma_score: str
