from src.settings import TASK_LABEL_NAME_MAP
from typing import Any, Dict, Generator, Iterable


def get_task_name(task_label: str) -> str:
    return TASK_LABEL_NAME_MAP[task_label]


def iter_dto_as_dicts(dto_iterable: Iterable) -> Generator[Dict[str, Any], None, None]:
    yield from map(lambda dto: dto.model_dump(), dto_iterable)
