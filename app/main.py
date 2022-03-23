from fastapi import FastAPI, Depends

from app import api
from app.config import Settings, get_settings
from app.core.generate import create_roles, create_super_admin
from app.secuirity.database import init_models

app = FastAPI()
app.include_router(api.api_router)


@app.on_event("startup")
def on_startup():
    init_models()
    create_roles()
    create_super_admin()


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "env": settings.env,
        "db": settings.db,
        "admin_email": settings.admin_email
    }
