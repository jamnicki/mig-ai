from src.settings import TASK_NUM_NAME_MAP


def get_task_name(task_num: str | int) -> str:
    return TASK_NUM_NAME_MAP[str(task_num)]
