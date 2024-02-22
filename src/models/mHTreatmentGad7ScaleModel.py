from pydantic import BaseModel, Field
import uuid


class MentalHealthGad7ScaleModel(BaseModel):
    feelingNervousAnxious: str
    notAbleToStopWorrying: str
    worryingTooMuch: str
    troubleRelaxing: str
    restlessDifficultySittingStill: str
    easilyAnnoyedIrritable: str
    feelingAfraidSomethingAwfulMightHappen: str
