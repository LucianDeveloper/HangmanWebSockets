from fastapi_users.authentication import CookieAuthentication
from typing import Optional
from fastapi import Response, WebSocket, Cookie, Query, status
from fastapi_users import FastAPIUsers
from src.users.schemas import *
from fastapi import Depends
from config import SECRET


async def get_cookie_or_token(
    websocket: WebSocket,
    session: Optional[str] = Cookie(None),
    token: Optional[str] = Query(None),
):
    if session is None and token is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    return session or token


cookie_authentication = CookieAuthentication(
    secret=SECRET,
    lifetime_seconds=3600,
    cookie_secure=False,
    cookie_httponly=False,
    cookie_domain='127.0.0.1',
)

fastapi_users = FastAPIUsers(
    user_db,
    [cookie_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)


fastapi_cookies = fastapi_users.get_auth_router(cookie_authentication)


@fastapi_cookies.post("/refresh")
async def refresh_jwt(response: Response, user=Depends(fastapi_users.get_current_active_user)):
    return await cookie_authentication.get_login_response(user, response)
