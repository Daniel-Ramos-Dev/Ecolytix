from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from database import SessionLocal, SensorData
from ai_engine import generate_insight
from blockchain import generate_hash

app = FastAPI()

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# MEMÓRIA TEMPORÁRIA
# =========================

latest_data = {
    "air_quality": 0,
    "status": "WAITING",
    "insight": "Waiting sensor data...",
    "tx_hash": "-"
}

# =========================
# MODEL
# =========================

class SensorPayload(BaseModel):
    air_quality: int
    status: str

# =========================
# ROOT
# =========================

@app.get("/")
def root():

    return {
        "project": "Ecolytix",
        "status": "running"
    }

# =========================
# RECEIVE SENSOR DATA
# =========================

@app.post("/api/sensor-data")
def receive_sensor_data(payload: SensorPayload):

    global latest_data

    insight = generate_insight(payload.air_quality)

    tx_hash = generate_hash({
        "air_quality": payload.air_quality,
        "status": payload.status
    })

    db = SessionLocal()

    record = SensorData(
        air_quality=payload.air_quality,
        status=payload.status,
        tx_hash=tx_hash
    )

    db.add(record)
    db.commit()

    latest_data = {
        "air_quality": payload.air_quality,
        "status": payload.status,
        "insight": insight,
        "tx_hash": tx_hash
    }

    return {
        "success": True,
        "data": latest_data
    }

# =========================
# GET LATEST DATA
# =========================

@app.get("/api/latest")
def get_latest():

    return latest_data