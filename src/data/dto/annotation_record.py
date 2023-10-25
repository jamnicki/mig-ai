from pydantic import BaseModel


class AnnotationRecord(BaseModel):
    start: int
    end: int
    text: str
    doc_filepath: str
    video_filename: str
    task_label: str


class GlossAnnotationRecord(AnnotationRecord):
    dominant_hand: bool = True


class PolishAnnotationRecord(AnnotationRecord):
    pass
