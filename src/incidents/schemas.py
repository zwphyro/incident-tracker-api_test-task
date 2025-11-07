from datetime import datetime

from pydantic import BaseModel, Field

from src.incidents.enums import IncidentStatusEnum, IncidentSourceEnum


class CreateIncidentSchema(BaseModel):
    description: str = Field(..., max_length=500)
    source: IncidentSourceEnum


class UpdateIncidentStatusSchema(BaseModel):
    status: IncidentStatusEnum


class IncidentResponseSchema(BaseModel):
    id: int
    description: str
    source: IncidentSourceEnum
    status: IncidentStatusEnum
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
