from fastapi import APIRouter
from app.services.queue_service import queue

router = APIRouter(prefix="/analytics")


@router.get("/stats")
def get_stats():

    stats = {
        "emergency": 0,
        "high": 0,
        "medium": 0,
        "low": 0
    }

    for patient in queue:

        severity = patient["severity"]

        if severity == "Emergency":
            stats["emergency"] += 1

        elif severity == "High":
            stats["high"] += 1

        elif severity == "Medium":
            stats["medium"] += 1

        elif severity == "Low":
            stats["low"] += 1

    return stats