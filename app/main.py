import os
from functools import lru_cache

from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from app import api
from app.config import Settings, ProdSettings, DevSettings

app = FastAPI()
app.include_router(api.api_router)


@lru_cache()
def get_settings():
    load_dotenv()
    return DevSettings() if Settings().env == 'dev' else ProdSettings()


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "env": settings.env,
        "db": settings.db,
    }
