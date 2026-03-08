from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import patient_routes, triage_routes, analytics_routes
from app.routes import diagnosis_routes
from app.routes import analytics_routes
from app.routes import prescription_routes
from app.routes import doctor_routes
from app.routes import billing_routes

app = FastAPI(title="MedFlow AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient_routes.router)
app.include_router(triage_routes.router)
app.include_router(diagnosis_routes.router)
app.include_router(analytics_routes.router)
app.include_router(prescription_routes.router)
app.include_router(doctor_routes.router)
app.include_router(billing_routes.router)


@app.get("/")
def root():
    return {"system":"MedFlow AI Running"}