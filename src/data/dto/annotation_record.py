from typing import Optional

from pydantic import BaseModel


class AnnotationRecord(BaseModel):
    start: int
    end: int
    text: str
    doc_filepath: str
    video_filename: str
    task_label: str


class GlosaAnnotationRecord(AnnotationRecord):
    dominant_hand: bool = True


class PolishAnnotationRecord(AnnotationRecord):
    pass
