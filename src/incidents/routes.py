from fastapi import APIRouter, HTTPException, status

from src.incidents import service
from src.incidents.enums import IncidentStatusEnum
from src.incidents.exceptions import IncidentNotFoundException
from src.incidents.schemas import (
    CreateIncidentSchema,
    IncidentResponseSchema,
    UpdateIncidentStatusSchema,
)
from src.dependencies import DBDependency
from src.schemas import HTTPExceptionSchema


router = APIRouter()


@router.post("/", response_model=IncidentResponseSchema)
async def create_incident(incident_data: CreateIncidentSchema, session: DBDependency):
    incident = await service.create_incident(
        session=session,
        description=incident_data.description,
        source=incident_data.source,
    )

    return incident


@router.get("/", response_model=list[IncidentResponseSchema])
async def list_incidents(
    session: DBDependency, status: IncidentStatusEnum | None = None
):
    incidents = await service.list_incidents(session=session, status=status)

    return incidents


@router.put(
    "/{incident_id}/status/",
    response_model=IncidentResponseSchema,
    responses={status.HTTP_404_NOT_FOUND: {"model": HTTPExceptionSchema}},
)
async def update_incident_status(
    incident_id: int, status_update: UpdateIncidentStatusSchema, session: DBDependency
):
    try:
        incident = await service.update_incident_status(
            session=session,
            incident_id=incident_id,
            new_status=status_update.status,
        )
    except IncidentNotFoundException:
        raise HTTPException(status_code=404, detail="Incident not found")

    return incident
