from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from fastapi import Depends
from src.users.websocket_auth import get_cookie_or_token
from src.users.schemas import User
from src.game.connection_manager import game_manager


ws_router = APIRouter()


@ws_router.websocket("/ws")
async def websocket_endpoint(
        websocket: WebSocket, user: str = Depends(get_cookie_or_token)
):
    await game_manager.connect(websocket, None)
    try:
        while True:
            data = await websocket.receive_json()
            await game_manager.new_game_action(websocket, data, user)
    except WebSocketDisconnect:
        game_manager.disconnect(websocket)
