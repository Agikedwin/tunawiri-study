from pydantic import BaseModel,Field
import uuid

class SocialSupportModel(BaseModel):
        id: object = Field(default_factory=uuid.uuid4, alias='_id')
        mchNumber: int
        insultedFeelings: str
        belittledHumiliated: str
        scareIntimidate: str
        threwOutHouse: str
        confinedLocked: str
        threatenedHurt: str
        slappedThrown: str
        pushedShoved: str
        hitWithFist: str
        kickedDragged: str
        chokedBurnt: str
        threatenedUsedWeapon: str
        forcedSexualIntercourse: str
        agreedUnwantedIntercourse: str
        forcedOtherSexualAct: str
        triedKeepFromFriends: str
        triedRestrictFamilyContact: str
        insistedKnowingLocation: str
        jealousAngryWithMen: str
        suspiciousUnfaithful: str
        tookEarningsSavings: str
        refusedMoneyForHousehold: str
        triedConvinceCrazy: str
        blamedForViolentBehavior: str