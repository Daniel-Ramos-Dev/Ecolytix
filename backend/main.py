from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_data = {
    "air_quality": 0,
    "status": "UNKNOWN"
}

@app.post('/api/sensor-data')
async def sensor_data(data: dict):

    global latest_data

    latest_data = data

    return {
        "success": True
    }

@app.get('/api/latest')
async def latest():
    return latest_data