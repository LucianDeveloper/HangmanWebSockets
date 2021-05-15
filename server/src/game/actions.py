import uuid
from typing import List, Optional


def format_template(
        is_disconnect, used_chars,
        pair_id, wait_word,
        is_run, word, answer,
        you_player=True,
        is_finish=False,
        lifes=0
):
    return {
        "is_disconnect": is_disconnect,
        "pair_id": pair_id,
        "wait_word": wait_word,
        "is_run": is_run,
        "word": word,
        "answer": answer,
        "used_chars": used_chars,
        "you_player": you_player,
        "new_char": None,
        "is_finish": is_finish,
        "lifes": lifes
    }


async def action(
        pair_id: uuid.UUID,
        word: str,
        answer: List[str],
        used_chars: List[str],
        lifes: int,
        wait_word: bool = False,
        is_run: bool = True,
        you_player: Optional[bool] = True,
        is_finish: Optional[bool] = False
):
    return format_template(
        is_disconnect=False,
        pair_id=pair_id,
        wait_word=wait_word,
        is_run=is_run,
        word=word,
        answer=answer,
        used_chars=used_chars,
        you_player=you_player,
        is_finish=is_finish,
        lifes=lifes
    )


async def connect_single():
    return format_template(
        is_disconnect=False,
        pair_id=None,
        wait_word=False,
        is_run=False,
        word="",
        answer=[],
        used_chars=[]
    )


async def disconnect(word):
    return format_template(
        is_disconnect=True,
        pair_id=None,
        wait_word=False,
        is_run=True,
        word=word,
        answer=[],
        used_chars=[]
    )
