from typing import List
from fastapi import WebSocket
from src.users.schemas import User
from src.game.pair import Pair
from src.game.connection import Connection
from src.game import actions


class ConnectionManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConnectionManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.users_without_pair: List[Connection] = []
        self.pairs: List[Pair] = []

    async def connect(self, websocket: WebSocket, user: User):
        await websocket.accept()
        if len(self.users_without_pair) > 0:
            connection = self.users_without_pair.pop(0)
            pair = Pair(connection.ws, connection.user, websocket, user)
            self.pairs.append(pair)
            await pair.start()
        else:
            new_conn = Connection(websocket, user)
            self.users_without_pair.append(new_conn)
            await websocket.send_json(await actions.connect_single())

    async def new_game_action(self, websocket: WebSocket, data: dict, user: User):
        pair = await self.get_pair(data['pair_id'])
        if pair is None:
            return None
        if data['wait_word']:
            word = data['word']
            if word is not None and len(word) > 1:
                await pair.set_word(word)
        elif data['new_char'] is not None:
            await pair.get_new_letter(data['new_char'])

    async def get_pair(self, pair_id: str):
        for pair in self.pairs:
            if await pair.is_pair_by_id(pair_id):
                return pair
        return None

    async def disconnect(self, websocket: WebSocket):
        if websocket in self.users_without_pair:
            self.users_without_pair.remove(websocket)
            return
        for pair in self.pairs:
            if await pair.is_pair_by_ws(websocket):
                await pair.disconnect()
                self.pairs.remove(pair)
                return


manager = ConnectionManager()
