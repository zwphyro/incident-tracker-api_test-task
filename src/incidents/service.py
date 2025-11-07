from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.incidents.enums import IncidentStatusEnum, IncidentSourceEnum
from src.incidents.models import Incident
from src.incidents.exceptions import IncidentNotFoundException


async def create_incident(
    session: AsyncSession, description: str, source: IncidentSourceEnum
):
    incident = Incident(description=description, source=source)

    session.add(incident)
    await session.commit()

    return incident


async def list_incidents(
    session: AsyncSession, status: IncidentStatusEnum | None = None
):
    query = select(Incident)
    if status:
        query = query.where(Incident.status == status)
    result = await session.execute(query)

    incidents = result.scalars().all()
    return incidents


async def update_incident_status(
    session: AsyncSession, incident_id: int, new_status: str
):
    incident = await session.get(Incident, incident_id)

    if not incident:
        raise IncidentNotFoundException

    incident.status = new_status

    await session.commit()

    return incident
