from fastapi import APIRouter
from app.database import billing_collection

router = APIRouter(prefix="/billing")


@router.post("/create")
def create_bill(data: dict):

    bill = {
        "patient": data["patient"],
        "amount": data["amount"],
        "description": data["description"]
    }

    billing_collection.insert_one(bill)

    return {"message": "Bill generated"}