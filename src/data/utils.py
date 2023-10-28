from typing import Any, Dict, Generator, Iterable

# from src.settings import TASK_NUM_NAME_MAP


# def get_task_name(task_num: str | int) -> str:
#     return TASK_NUM_NAME_MAP[str(task_num)]


def iter_dto_as_dicts(dto_iterable: Iterable) -> Generator[Dict[str, Any], None, None]:
    yield from map(lambda dto: dto.model_dump(), dto_iterable)
