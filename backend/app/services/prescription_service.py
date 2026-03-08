from app.database import prescriptions_collection


def create_prescription(patient_name, diagnosis, medicines):

    record = {
        "patient": patient_name,
        "diagnosis": diagnosis,
        "medicines": medicines
    }

    # insert into MongoDB
    result = prescriptions_collection.insert_one(record)

    # convert ObjectId to string
    record["_id"] = str(result.inserted_id)

    return record


def get_prescriptions():

    prescriptions = []

    # fetch all prescriptions
    for p in prescriptions_collection.find():

        # convert MongoDB ObjectId to string
        p["_id"] = str(p["_id"])

        prescriptions.append(p)

    return prescriptions