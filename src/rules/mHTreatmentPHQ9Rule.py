from fastapi import BackgroundTasks, Request, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.mHTreatmentPHQ9Model import MentalHealthPHQ9Model
from bson import ObjectId


def getcollection_mental_health_phq9(request: Request):
    return request.app.database['mentalhealthPhq9']


def create_mental_health_phq9(request: Request, mentalhealthPhq9: MentalHealthPHQ9Model = Body(...)):
    new_mental = getcollection_mental_health_phq9(request).insert_one(jsonable_encoder(mentalhealthPhq9))
    return getcollection_mental_health_phq9(request).find_one({"_id": new_mental.inserted_id})


def list_mental_health_phq9(request: Request, limit: int):
    return list(getcollection_mental_health_phq9(request).find(limit=limit))


def find_one_mental_health_phq9(request: Request, user_id: object):
    print("PHQ9 ---")
    if mental := getcollection_mental_health_phq9(request).find_one({"user_id": user_id}):
        return mental
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Metal Health Phq9 with Id {id} not found")


def delete_menta_health_phq9(request: Request, id: str):
    if getcollection_mental_health_phq9(request).delete_one({"_id": ObjectId(id)}).deleted_count == 1:
        return f"Mental Health Phq9  with id {id}  deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Mental Health Phq9 with id {id} not found")
