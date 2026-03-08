from fastapi import APIRouter

router = APIRouter(prefix="/doctors")

doctors = [
    {"name": "Dr. Kumar", "status": "available"},
    {"name": "Dr. Priya", "status": "available"},
    {"name": "Dr. Arjun", "status": "available"}
]


@router.get("/list")
def get_doctors():
    return doctors


@router.post("/update")
def update_status(data: dict):

    for d in doctors:
        if d["name"] == data["name"]:
            d["status"] = data["status"]

    return {"message": "Doctor status updated", "doctors": doctors}