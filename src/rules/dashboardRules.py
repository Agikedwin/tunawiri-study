from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.dashboardModel import Dashboard
from  src.schemas.dashboard import serializeDict, serializeList

def get_collection_users(request: Request):
    return request.app.database['users']


def get_collection_clinicals(request: Request):
    return request.app.database['clinical']


def list_dashboard(request: Request, limit: int):
    return serializeList(get_collection_users(request).aggregate([
        {
            '$lookup': {
                'from': 'clinical',
                'pipeline': [],
                'as': 'clinical'
            }
        },
        {
            '$lookup': {
                'from': 'mentalhealthPhq9',
                'pipeline': [],
                'as': 'phq9'
            }
        },
        {
            '$lookup': {
                'from': 'mentalhealthGad7Scale',
                'pipeline': [],
                'as': 'gad7'
            }
        },
        {
            '$lookup': {
                'from': 'mentalhealthHarvardTrauma',
                'pipeline': [],
                'as': 'harvard'
            }
        },
        {
            '$lookup': {
                'from': 'mentalhealthSuicidal',
                'pipeline': [],
                'as': 'suicidal'
            }
        },
        {
            '$lookup': {
                'from': 'mentalhealthTraumaScale',
                'pipeline': [],
                'as': 'trauma'
            }
        },



    ]))
