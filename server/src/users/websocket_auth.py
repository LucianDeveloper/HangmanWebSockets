from typing import Optional
from fastapi import WebSocket, Cookie, Query, status


async def get_cookie_or_token(
    websocket: WebSocket,
    session: Optional[str] = Cookie(None),
):
    # if session is None and token is None:
    #     await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    print(session)
    return None
    return session or token
