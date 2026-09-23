from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

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

@app.get("/", include_in_schema=False)
@app.get("/temp_sensor_readings", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")


@app.get("/api/sensor_readings")
def get_sensor_readings():
    return sensor_readings
