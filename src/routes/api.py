from fastapi import APIRouter
from src.endpoints import (users, clinical,socialSupport, mHTreatmentGeneral, mHTreatmentAntenatal,
                           mHTreatmentPostnatal,mHTreatmentPHQ9, mHTreatmentGad7Scale,mHTreatmentTraumaExposure,
                           mHTreatmentHarvardTrauma,mHTreatmentSuicidal, home)

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

