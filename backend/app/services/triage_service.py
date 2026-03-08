# triage_service.py

from app.services.severity_mapping import get_severity


def triage_patient(symptoms):

    severity = get_severity(symptoms)

    return {
        "severity": severity
    }