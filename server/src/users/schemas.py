from fastapi_users import models
from tortoise import Tortoise
from tortoise.contrib.pydantic import PydanticModel
from fastapi_users.db import TortoiseUserDatabase
from config import DBPaths
from src.users.models import UserModel


Tortoise.init_models(DBPaths.users, 'models')


class User(models.BaseUser, PydanticModel):
    class Config:
        orm_mode = True
        orig_model = UserModel

    def __str__(self):
        return (
            '{'
            f'"email": "{self.email}",'
            f'"id": "{self.id}"'
            '}'
        )


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


user_db = TortoiseUserDatabase(UserDB, UserModel)
