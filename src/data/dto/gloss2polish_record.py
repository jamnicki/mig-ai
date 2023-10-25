from typing import List

from pydantic import BaseModel

from .annotation_record import GlossAnnotationRecord, PolishAnnotationRecord


class GlossSeq2PolishRecord(BaseModel):
    gloss_sequence: List[GlossAnnotationRecord]
    polish_annotation: PolishAnnotationRecord

    @staticmethod
    def from_dict(dict_):
        return GlossSeq2PolishRecord(
            gloss_sequence=[
                GlossAnnotationRecord(**gloss) for gloss in dict_["gloss_sequence"]
            ],
            polish_annotation=PolishAnnotationRecord(**dict_["polish_annotation"]),
        )
