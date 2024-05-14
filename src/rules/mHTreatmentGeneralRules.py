from  fastapi import BackgroundTasks, Request, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.mHTreatmentGeneralModel import GeneralTreatmentModel
from bson import ObjectId

def getcollection_mental_heelth(request: Request):
    return request.app.database['maternalandinfanthealth']

def create_mental_health(request:Request, mentalhealth: GeneralTreatmentModel=Body(...)):
    new_mental = getcollection_mental_heelth(request).insert_one(jsonable_encoder(mentalhealth))
    return getcollection_mental_heelth(request).find_one({"_id": new_mental.inserted_id})

def list_mental_health(request: Request, limit: int):
    return list(getcollection_mental_heelth(request).find(limit=limit))

def find_one_mental_health(request: Request, user_id: object):
    if (mental:= getcollection_mental_heelth(request).find({"user_id": user_id}).sort({'created_at': -1})):
        return mental
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Metal Health with Id {id} not found")
def delete_menta_health(request: Request, id: str):
    if getcollection_mental_heelth(request).delete_one({"_id": ObjectId(id)}).deleted_count == 1:
        return f"Mental Health with id {id}  deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Mental Health with id {id} not found")