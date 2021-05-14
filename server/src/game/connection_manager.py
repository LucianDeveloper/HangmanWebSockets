from typing import List
from fastapi import WebSocket
from uuid import UUID


class Pair:
    def __init__(
            self,
            first_user: WebSocket,
            first_id: int,
            second_user: WebSocket,
            second_id: int
    ):
        self.__id = UUID()
        self.__first_ws = first_user
        self.__first_id = first_id
        self.__second_ws = second_user
        self.__second_id = second_id
        self.__wait_word = True
        self.__is_first = True
        self.__is_run = True

    async def send_action(self, action):
        pass
        # await self.__first_ws.send_json()
        # await self.__second_ws.send_json()

    async def disconnect(self):
        pass
        # ToDO disconnect
        # await self.send_action(disconnect)

    async def get_users_ws(self):
        return self.__first_ws, self.__second_ws

    async def is_pair_by_id(self, check_id: int):
        return check_id == self.__first_id or check_id == self.__second_id

    @property
    def is_wait_word(self):
        return self.__wait_word

    @property
    def is_step_first(self):
        return self.__is_first

    @property
    def is_run(self):
        return self.__is_run

    @property
    def id(self):
        return self.__id


class ConnectionManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConnectionManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.users_without_pair: List[WebSocket] = []
        self.pairs: List[Pair] = []

    async def connect(self, websocket: WebSocket, client_id: int):
        await websocket.accept()
        if len(self.users_without_pair) > 0:
            ws = self.users_without_pair.pop(0)
            # ToDO add with client_id
            pair = Pair(ws, None, websocket, None)
            self.pairs.append(pair)
            # ToDO send connect action
            # ToDO await pair.send_action(action)
        else:
            self.users_without_pair.append(websocket)

    async def disconnect(self, websocket: WebSocket, client_id: int):
        if websocket in self.users_without_pair:
            self.users_without_pair.remove(websocket)
            return
        for pair in self.pairs:
            if await pair.is_pair_by_id(client_id):
                # ToDo send disconnect
                # pair.disconnect()
                self.pairs.remove(pair)
                return


manager = ConnectionManager()
