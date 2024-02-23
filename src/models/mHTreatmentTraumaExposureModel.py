from pydantic import BaseModel, Field
import uuid


class MentalHealthTraumaExposureModel(BaseModel):
    witnessedMurderOfFamilyOrFriend: str
    witnessedMurderOfStrangerOrKnownPerson: str
    witnessedArmedAttackOnSomeone: str
    leftCountryDueToWarConflictPoverty: str
    sexuallyAssaultedOrRaped: str
    experiencedTorture: str
    robbedAtGunpointOrKnifePoint: str
    kidnapped: str
    feltCloseToDeath: str
    witnessedSomeoneBeingRaped: str
    trauma_exposure_score: str
