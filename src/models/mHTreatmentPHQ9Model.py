from pydantic import BaseModel, Field
import uuid


class MentalHealthPHQ9Model(BaseModel):
    interestPleasure: str
    feelingDepressed: str
    troubleSleeping: str
    feelingTired: str
    poorAppetite: str
    feelingBadAboutYourself: str
    troubleConcentrating: str
    slowOrRestless: str
    thoughtsOfHarmingYourself: str
    difficultyExperiencedProblems: str
