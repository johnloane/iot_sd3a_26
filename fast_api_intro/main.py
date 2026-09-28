from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


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


@app.get("/readings/{reading_id}", include_in_schema=False)
def reading_page(request: Request, reading_id: int):
    for reading in sensor_readings:
        if reading.get("id") == reading_id:
            title = reading["sensor"][:50]
            return templates.TemplateResponse(request, "reading.html", {"reading":reading, "title": title})
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Sensor reading not found")


@app.get("/api/sensor_readings")
def get_sensor_readings():
    return sensor_readings


@app.get("/api/readings/{reading_id}")
def get_reading(reading_id: int):
    for reading in sensor_readings:
        if reading.get("id") == reading_id:
            return reading
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Sensor reading not found")




@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request:Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail
        else "An error occurred. Please check your request and try again"
    )
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code = exception.status_code,
            content = {"detail":message},
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code" : exception.status_code,
            "title" : exception.status_code,
            "message" : message,
        },
        status_code = exception.status_code,
    )
    
    
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request:Request, exception:RequestValidationError):
    if request.url.path.startswith("/api"):
            return JSONResponse(
                status_code = status.HTTP_422_UNPROCESSABLE_CONTENT,
                content = {"detail":exception.errors()},
            )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code" : status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title" : status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message" : "Invalid request. Please check your input and try again",
        },
        status_code = status.HTTP_422_UNPROCESSABLE_CONTENT,
    )
