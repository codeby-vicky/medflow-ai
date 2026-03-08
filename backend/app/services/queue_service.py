from app.services.wait_time_model import predict_wait_time


priority_map = {
    "Emergency": 4,
    "High": 3,
    "Medium": 2,
    "Low": 1
}


queue = []


def add_patient(patient):

    # normalize severity text
    patient["severity"] = patient["severity"].strip().title()

    queue.append(patient)

    # sort patients by severity priority then arrival time
    queue.sort(
        key=lambda p: (
            -priority_map.get(p["severity"], 2), 
            p["arrival_time"]
        )
    )

    update_wait_times()

    return queue



def update_wait_times():

    for index, patient in enumerate(queue):

        patient["estimated_wait"] = predict_wait_time(index + 1)