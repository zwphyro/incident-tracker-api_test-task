from enum import StrEnum


class IncidentStatusEnum(StrEnum):
    OPEN = "open"
    REOPENED = "reopened"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class IncidentSourceEnum(StrEnum):
    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"
    CUSTOMER = "customer"
