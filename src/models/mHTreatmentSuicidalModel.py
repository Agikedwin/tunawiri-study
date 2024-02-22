
from pydantic import BaseModel, Field
import uuid


class MentalHealthSuicidalModel(BaseModel):
    wishedDeadOrToSleep: str
    thoughtsAboutKillingYourself: str
    thinkingAboutHowToKillYourself: str
    thoughtsWithIntentionOfActing: str
    workedOutDetailsOfKillingYourself: str
    doneAnythingToEndYourLife3month: str
    doneAnythingToEndYourLifeLifetime: str
    suicidalScreenerScore: str