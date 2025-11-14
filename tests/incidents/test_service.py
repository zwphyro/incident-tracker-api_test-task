import pytest
from unittest.mock import AsyncMock, Mock

import src.incidents.service as incident_service
from src.incidents.enums import IncidentSourceEnum


@pytest.fixture
def session_mock():
    session = AsyncMock()
    session.add = Mock()
    session.commit = AsyncMock()
    return session


@pytest.mark.asyncio
async def test_create_incident_ok(session_mock: AsyncMock):
    description = "Test incident"
    source = IncidentSourceEnum.CUSTOMER

    incident = await incident_service.create_incident(
        session=session_mock, description=description, source=source
    )

    session_mock.add.assert_called_once_with(incident)
    session_mock.commit.assert_awaited_once()
    assert incident.description == description
    assert incident.source == source
