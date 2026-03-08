
def simple_stats(patients):
    total = len(patients)
    emergency = len([p for p in patients if p["severity"]=="Emergency"])
    return {"total_patients":total,"emergency_cases":emergency}
