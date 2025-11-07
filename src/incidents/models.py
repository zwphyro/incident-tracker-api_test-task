from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base
from src.incidents.enums import IncidentStatusEnum


class Incident(Base):
    status: Mapped[str] = mapped_column(default=IncidentStatusEnum.OPEN, nullable=False)
    source: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
