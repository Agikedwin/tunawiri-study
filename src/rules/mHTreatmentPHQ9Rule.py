from fastapi import BackgroundTasks, Request, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.mHTreatmentPHQ9Model import MentalHealthPHQ9Model
from bson import ObjectId

from datetime import datetime


def getcollection_mental_health_phq9(request: Request):
    return request.app.database['mentalhealthPhq9']


def create_mental_health_phq9(request: Request, mentalhealthPhq9: MentalHealthPHQ9Model = Body(...)):
    new_mental = getcollection_mental_health_phq9(request).insert_one(jsonable_encoder(mentalhealthPhq9))
    return getcollection_mental_health_phq9(request).find_one({"_id": new_mental.inserted_id})


def list_mental_health_phq9(request: Request, limit: int):
    return list(getcollection_mental_health_phq9(request).find(limit=limit))


def find_one_mental_health_phq9(request: Request, user_id: object):
    print("PHQ9 ---")
    if mental := getcollection_mental_health_phq9(request).find({"user_id": user_id}).sort({'created_at': -1}):
        return mental
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Metal Health Phq9 with Id {id} not found")


def delete_menta_health_phq9(request: Request, id: str):
    if getcollection_mental_health_phq9(request).delete_one({"_id": ObjectId(id)}).deleted_count == 1:
        return f"Mental Health Phq9  with id {id}  deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Mental Health Phq9 with id {id} not found")


def find_phq9_gad7_graph(request: Request, user_id: object):
    format_string = "%Y-%m-%d"
    pipeline = [
        {
            '$lookup': {
                'from': 'mentalhealthGad7Scale',
                'localField': 'user_id',
                'foreignField': 'user_id',
                'as': 'gad7'
            }
        },
        {
            '$unwind': '$gad7'
        },

        {
            '$match': {
                'user_id': {'$eq': user_id}
            }
        },

    ]

    if graph := getcollection_mental_health_phq9(request).aggregate(pipeline):
        phq9 = []
        gad7 = []
        visit_count = []
        count = 0
        for data in graph:
            count+=1
            phq9.append(data['phq9_score'])
            gad7.append(data['gad7']['gad7_score'])
            if  data['created_at']:
                #visit_count.append(f"Visit {count}" )
                visit_count.append(data['created_at'][0:10])
            else:
                visit_count.append(data['gad7']['created_at'][0:10])

        print(gad7,phq9,visit_count)

        return  {
            'phq9': phq9,
            'gad7' : gad7,
            'visit' : visit_count
        }

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" Graph data for id  {id} not found")
