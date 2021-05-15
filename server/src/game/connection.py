from fastapi import WebSocket
from src.users.schemas import User


class Connection:
    def __init__(self, ws: WebSocket, user: User):
        self.ws: WebSocket = ws
        self.user: User = user
