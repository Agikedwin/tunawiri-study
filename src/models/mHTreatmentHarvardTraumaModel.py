from pydantic import BaseModel, Field
import uuid


class MentalHealthHarvardTraumaModel(BaseModel):
    thoughtsMemories: str
    feelingAsThoughEventHappeningAgain: str
    recurrentNightmares: str
    feelingDetachedWithdrawn: str
    unableToFeelEmotions: str
    feelingJumpyEasilyStartled: str
    difficultyConcentrating: str
    troubleSleeping: str
    feelingOnGuard: str
    feelingIrritableOrAngry: str
    avoidingActivitiesRemindOfEvent: str
    inabilityToRememberTraumaticEvents: str
    lessInterestInDailyActivities: str
    feelingNoFuture: str
    suddenEmotionalPhysicalReaction: str
    avoidingThoughtsFeelingsAssociatedWithEvent: str
    feelingWorldIsDangerousPlace: str
    feelingYouAreBadPerson: str
    blamingYourselfForTraumaticEvent: str
    strongFeelingOfFearHorrorAngerGuiltShame: str
    difficultyFeelingLoveOrHappiness: str
    takingRisksThatMayHarmYourselfOrOthers: str
    feelingDamagedByTraumaticEvent: str
    feelingSomethingRemindsYouOfTraumaLikeADream: str
    feelingPeopleOrObjectsAroundYouAreStrangeOrNotReal: str
    harvardTraumaScore: int
