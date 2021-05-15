from typing import List
from fastapi import WebSocket
import uuid
from src.users.schemas import User
from src.game.actions import action, disconnect


class Pair:
    def __init__(
        self,
        first_user: WebSocket,
        f_user: User,
        second_user: WebSocket,
        s_user: User,
    ):
        self.__id = uuid.uuid4()
        self.__first_user = f_user
        self.__first_ws = first_user
        self.__second_user = s_user
        self.__second_ws = second_user
        self.__wait_word = True
        self.__word = None
        self.__answer: List[str] = []
        self.__used_chars: List[str] = []
        self.__is_run = True
        self.__is_finish = False
        self.__lifes = 8

    def dict(self) -> dict:
        return {
            'pair_id': str(self.__id),
            'word': self.__word,
            'wait_word': self.__wait_word,
            'used_chars': self.__used_chars,
            'is_run': self.is_run,
            'answer': self.__answer,
            'lifes': self.__lifes,
            'is_finish': self.__is_finish
        }

    async def refresh(self):
        await self.refresh_answer()
        await self.__first_ws.send_json(await action(you_player=False, **self.dict()))
        await self.__second_ws.send_json(await action(you_player=True, **self.dict()))

    async def refresh_answer(self):
        self.__answer = list(map(
            lambda char: char if char in self.__used_chars else '_',
            self.__word
        ))

    async def set_word(self, word: str):
        if self.__wait_word:
            self.__word = word
            self.__wait_word = False
            await self.refresh()

    async def get_new_letter(self, letter: str):
        if letter not in self.__used_chars:
            self.__used_chars.append(letter)
            if letter in self.__word:
                await self.refresh_answer()
                if '_' not in self.__answer:
                    return await self.finish()
            else:
                self.__lifes -= 1
                if self.__lifes == 0:
                    return await self.finish()
            await self.refresh()

    async def is_pair_by_ws(self, ws: WebSocket):
        return self.__first_ws == ws or self.__second_ws == ws

    async def is_pair_by_id(self, pair_id: str):
        return str(self.__id) == pair_id

    async def start(self):
        await self.__first_ws.send_json(await action(you_player=False, **self.dict()))
        await self.__second_ws.send_json(await action(you_player=True, **self.dict()))

    async def finish(self):
        self.__is_finish = True
        await self.refresh()

    @property
    def is_finish(self):
        return self.__is_finish

    async def disconnect(self):
        await self.__first_ws.send_json(await disconnect(self.__word))
        await self.__second_ws.send_json(await disconnect(self.__word))

    async def get_users_ws(self):
        return self.__first_ws, self.__second_ws

    @property
    def is_wait_word(self):
        return self.__wait_word

    @property
    def is_run(self):
        return self.__is_run

    @property
    def id(self):
        return self.__id
