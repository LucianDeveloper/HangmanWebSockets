from os import environ


class DBPaths:
    users = ['src.users.models']

    all_paths = users


DB_URL = environ.get('DB_URL', "sqlite://sql_app.db")
URL = environ.get('URL', "http://localhost:8000")
WS_URL = environ.get('WS_URL', "ws://localhost:8000")

SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
