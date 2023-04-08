from fastapi import FastAPI
from app.routes import weather_route

app = FastAPI()

app.include_router(weather_route.router)
