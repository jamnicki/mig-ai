from typing import List

from pydantic import BaseModel

from .annotation_record import PolishAnnotationRecord


class ImgSeq2PolishRecord(BaseModel):
    img_filepath_sequence: List[str]
    polish_annotation: PolishAnnotationRecord

    @staticmethod
    def from_dict(dict_: dict):
        return ImgSeq2PolishRecord(
            img_filepath_sequence=dict_["img_filepath_sequence"],
            polish_annotation=PolishAnnotationRecord(**dict_["polish_annotation"]),
        )
