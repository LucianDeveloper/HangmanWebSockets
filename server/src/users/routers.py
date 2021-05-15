from fastapi_users.authentication import CookieAuthentication
from fastapi import Response
from fastapi_users import FastAPIUsers
from src.users.schemas import *
from fastapi import Depends
from config import SECRET


cookie_authentication = CookieAuthentication(
    secret=SECRET,
    lifetime_seconds=3600,
    cookie_secure=False,
    cookie_httponly=False,
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
