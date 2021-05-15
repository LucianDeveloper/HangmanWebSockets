from config import DB_URL, DBPaths
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from src.game.routers import ws_router

from src.users.routers import (
    fastapi_cookies,
    fastapi_users,
    SECRET,
)
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(
    title='HangMan WebSockets',
    description="API with WS for game HangMan",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(
    fastapi_cookies, prefix="/auth/jwt", tags=["Auth"]
)
app.include_router(
    fastapi_users.get_register_router(), prefix="/auth", tags=["Auth"]
)
app.include_router(
    fastapi_users.get_reset_password_router(SECRET),
    prefix="/auth", tags=["Auth"],
)

app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["Пользователи"])

app.include_router(ws_router)

app.mount("/static", StaticFiles(directory="static"), name="static")


register_tortoise(
    app,
    db_url=DB_URL,
    modules={"models": DBPaths.all_paths},
    generate_schemas=True,
    add_exception_handlers=True,
)
