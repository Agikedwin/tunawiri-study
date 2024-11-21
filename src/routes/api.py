from fastapi import APIRouter
from src.endpoints import (users, clinical, socialSupport, mHTreatmentGeneral, mHTreatmentAntenatal,
                           mHTreatmentPostnatal, mHTreatmentPHQ9, mHTreatmentGad7Scale, mHTreatmentTraumaExposure,
                           mHTreatmentHarvardTrauma, mHTreatmentSuicidal, ArtAdherence, MentalHealthTreatment,
                           TunawiriIntervention, MentalTreatment,login, dashboard, home, case_review_initial,case_review_followup, graphs)

router = APIRouter()

router.include_router(home.router)
router.include_router(users.router)
router.include_router(clinical.router)
router.include_router(socialSupport.router)
router.include_router(mHTreatmentGeneral.router)
router.include_router(mHTreatmentAntenatal.router)
router.include_router(mHTreatmentPostnatal.router)
router.include_router(mHTreatmentPHQ9.router)
router.include_router(mHTreatmentGad7Scale.router)
router.include_router(mHTreatmentTraumaExposure.router)
router.include_router(mHTreatmentHarvardTrauma.router)
router.include_router(mHTreatmentSuicidal.router)
router.include_router(ArtAdherence.router)
router.include_router(MentalHealthTreatment.router)
router.include_router(dashboard.router)
router.include_router(TunawiriIntervention.router)
router.include_router(MentalTreatment.router)
router.include_router(login.router)
router.include_router(case_review_followup.router)
router.include_router(case_review_initial.router)
router.include_router(graphs.router)