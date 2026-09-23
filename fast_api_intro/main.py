from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

sensor_readings: list[dict] = [
    {
        "id": 1,
        "sensor" : "temp",
        "content" : 21.0,
        "date_timestamp" : "Sept 21, 2026, 13:00"
    },
    {
         "id": 2,
        "sensor" : "lux",
        "content" : 100,
        "date_timestamp" : "Sept 21, 2026, 13:05"
    }
]

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False, name="home")
@app.get("/temp_sensor_readings", include_in_schema=False, name = "temp_sensor_readings")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"sensor_readings":sensor_readings, "title":"IoT sensor readings"})


@app.get("/api/sensor_readings")
def get_sensor_readings():
    return sensor_readings


@app.get("/api/readings/{reading_id}")
def get_reading(request, reading_id: int):
    for reading in sensor_readings:
        if reading.get("id") == reading_id:
            return templates.TemplateResponse(request, "reading.html", {"reading":reading, "title":"IoT sensor readings"})
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Sensor reading not found")


@app.get("/readings/{reading_id}")
def reading_page(reading_id: int):
    for reading in sensor_readings:
        if reading.get("id") == reading_id:
            return reading
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Sensor reading not found")
