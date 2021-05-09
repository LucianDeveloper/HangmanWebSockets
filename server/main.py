from config import DB_URL, DBPaths
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, status
from fastapi import Depends
from src.users.schemas import User
from src.game.connection_manager import manager


from src.users.routers import (
    fastapi_jwt,
    fastapi_users,
    SECRET,
    get_cookie_or_token
)
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

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
    fastapi_jwt, prefix="/auth/jwt", tags=["Auth"]
)
app.include_router(
    fastapi_users.get_register_router(), prefix="/auth", tags=["Auth"]
)
app.include_router(
    fastapi_users.get_reset_password_router(SECRET),
    prefix="/auth", tags=["Auth"],
)

app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["Пользователи"])

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(
        websocket: WebSocket, client_id: int,
        cookie_or_token: str = Depends(get_cookie_or_token),
):
    if cookie_or_token is None:
        return
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


@app.get("/")
async def get():
    return HTMLResponse(html)


register_tortoise(
    app,
    db_url=DB_URL,
    modules={"models": DBPaths.all_paths},
    generate_schemas=True,
    add_exception_handlers=True,
)