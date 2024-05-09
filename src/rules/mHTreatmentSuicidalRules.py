from fastapi import BackgroundTasks, Request, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.mHTreatmentSuicidalModel import MentalHealthSuicidalModel
from bson import ObjectId


def getcollection_mental_health_suicidal(request: Request):
    return request.app.database['mentalhealthSuicidal']


def create_mental_health_suicidal(request: Request, mentalhealthSuicidal: MentalHealthSuicidalModel = Body(...)):
    new_mental = getcollection_mental_health_suicidal(request).insert_one(jsonable_encoder(mentalhealthSuicidal))
    return getcollection_mental_health_suicidal(request).find_one({"_id": new_mental.inserted_id})


def list_mental_health_suicidal(request: Request, limit: int):
    return list(getcollection_mental_health_suicidal(request).find(limit=limit))


def find_one_mental_health_suicidal(request: Request, user_id: str):
    if mental := getcollection_mental_health_suicidal(request).find_one({"user_id": user_id}):
        return mental
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Metal Health Suicidal with Id {id} not found")


def delete_menta_health_suicidal(request: Request, id: str):
    if getcollection_mental_health_suicidal(request).delete_one({"_id": ObjectId(id)}).deleted_count == 1:
        return f"Mental Health Suicidal  with id {id}  deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Mental Health Suicidal with id {id} not found")
