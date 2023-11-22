import re
from typing import Any, Dict, Generator, Iterable

from src.settings import TASK_LABEL_NAME_MAP


def get_task_name(task_label: str) -> str:
    return TASK_LABEL_NAME_MAP[task_label]


def iter_dto_as_dicts(dto_iterable: Iterable) -> Generator[Dict[str, Any], None, None]:
    yield from map(lambda dto: dto.model_dump(), dto_iterable)


def clean_gloss(gloss: str) -> str:
    out = re.sub(r"\d\.\d", "", gloss)
    out = re.sub(r"([\wØ]+[:;])+[\wØ]?[:;]?", "", out)
    out = re.sub(r"\d+\+\d+", "", out)
    out = re.sub(r"[\(\)\[\]]", "", out)
    out = re.sub(r"/", " ", out)
    out = re.sub(r"\$:", "", out)
    out = re.sub(r"\W", " ", out)
    out = re.sub(r"\s+", " ", out)
    return out
