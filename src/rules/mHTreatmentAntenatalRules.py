from fastapi import BackgroundTasks, Request, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.mHTreatmentDeliveryForm import MentalHealthDeliveryFormModel
from bson import ObjectId


def getcollection_mental_health_antenatal(request: Request):
    return request.app.database['mentalhealthAntenatal']


def create_mental_health_antenatal(request: Request, mentalhealthAntenatal: MentalHealthDeliveryFormModel = Body(...)):
    new_mental = getcollection_mental_health_antenatal(request).insert_one(jsonable_encoder(mentalhealthAntenatal))
    return getcollection_mental_health_antenatal(request).find_one({"_id": new_mental.inserted_id})


def list_mental_health_antenatal(request: Request, limit: int):
    return list(getcollection_mental_health_antenatal(request).find(limit=limit))


def find_one_mental_health_antenatal(request: Request, user_id: str):
    if mental := getcollection_mental_health_antenatal(request).find({"user_id": user_id}).sort({'created_at': -1}):
        return mental
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Metal Health Antenatal with Id {id} not found")


def delete_menta_health_antenatal(request: Request, id: str):
    if getcollection_mental_health_antenatal(request).delete_one({"_id": ObjectId(id)}).deleted_count == 1:
        return f"Mental Health Antenatal  with id {id}  deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Mental Health Antenatal with id {id} not found")
