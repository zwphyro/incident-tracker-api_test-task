from pydantic import BaseModel


class HTTPExceptionSchema(BaseModel):
    detail: str

    class Config:
        schema_extra = {"example": {"detail": "Incident not found"}}
