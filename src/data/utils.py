from src.settings import TASK_LABEL_NAME_MAP


def get_task_name(task_label: str) -> str:
    return TASK_LABEL_NAME_MAP[task_label]
