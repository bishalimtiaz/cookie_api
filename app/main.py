from functools import lru_cache

from dotenv import load_dotenv
from fastapi import FastAPI, Depends

from app import api
from app.config import Settings, ProdSettings, DevSettings
from app.core.generate import create_roles
from app.secuirity.database import init_models

app = FastAPI()
app.include_router(api.api_router)


@lru_cache()
def get_settings():
    load_dotenv()
    return DevSettings() if Settings().env == 'dev' else ProdSettings()


@app.on_event("startup")
async def on_startup():
    await init_models()
    await create_roles()


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "env": settings.env,
        "db": settings.db,
    }
