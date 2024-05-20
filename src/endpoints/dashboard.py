from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.dashboardModel import Dashboard
import src.rules.dashboardRules as dash
from  src.schemas.dashboard import serializeDict

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/", response_description="Get Dashboard data")
def list_dashboards(request: Request):
    return list(dash.list_dashboard(request, 10000))
