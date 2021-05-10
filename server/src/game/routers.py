from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from fastapi import Depends
from src.game.connection_manager import manager
from src.users.routers import get_cookie_or_token


ws_router = APIRouter()


@ws_router.websocket("/ws/{client_id}")
async def websocket_endpoint(
        websocket: WebSocket, client_id: int,
        # cookie_or_token: str = Depends(get_cookie_or_token),
):
    # if cookie_or_token is None:
    #     return
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
