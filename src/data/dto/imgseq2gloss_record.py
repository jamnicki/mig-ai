from typing import List

from pydantic import BaseModel

from .annotation_record import GlossAnnotationRecord


class ImgSeq2GlossRecord(BaseModel):
    img_filepath_sequence: List[str]
    gloss_annotation: GlossAnnotationRecord

    @staticmethod
    def from_dict(dict_: dict):
        return ImgSeq2GlossRecord(
            img_filepath_sequence=dict_["img_filepath_sequence"],
            gloss_annotation=GlossAnnotationRecord(**dict_["gloss_annotation"]),
        )
