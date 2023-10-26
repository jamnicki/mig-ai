from pathlib import Path
from typing import Callable, List

from jsonlines import jsonlines
from loguru import logger
from torch.utils.data import Dataset

from src.data.dto import (
    GlossAnnotationRecord,
    GlossSeq2PolishRecord,
    PolishAnnotationRecord,
)
from src.settings import (
    GLOSS_ANNOTATIONS_FPATH,
    GLOSSSEQ2POLISH_FILEPATH,
    POLISH_ANNOTATIONS_FPATH,
)


class GlossSeq2PolishDataset(Dataset):
    data_records: List[GlossSeq2PolishRecord]
    data_fpath: Path

    def __init__(
        self,
        data_fpath: Path = GLOSSSEQ2POLISH_FILEPATH,
    ):
        self.data_fpath = data_fpath
        self.data_records = list(
            map(GlossSeq2PolishRecord.from_dict, jsonlines.open(self.data_fpath))
        )

    def __len__(self):
        return len(self.data_records)

    def __getitem__(self, index) -> GlossSeq2PolishRecord:
        return self.data_records[index]


def collect_gloss_annotations(
    polish_annotation: PolishAnnotationRecord,
    gloss_annotations: List[GlossAnnotationRecord],
) -> List[GlossAnnotationRecord]:
    # TODO: optimize
    return [
        gloss_annotation
        for gloss_annotation in gloss_annotations
        if matching_gloss_annotation(gloss_annotation, polish_annotation)
    ]


def matching_gloss_annotation(
    gloss_annotation: GlossAnnotationRecord,
    polish_annotation: PolishAnnotationRecord,
) -> bool:
    # TODO: sprawdzic czy to ze glosa moze miec 2 taski dla jednego polskiego jest ok
    return (
        gloss_annotation.start >= polish_annotation.start
        and gloss_annotation.end <= polish_annotation.end
        and gloss_annotation.video_filename == polish_annotation.video_filename
        # and gloss_annotation.task_label == polish_annotation.task_label
    )


def dump_paired_dataset(callback: Callable, force=False, **kwargs):
    if GLOSSSEQ2POLISH_FILEPATH.exists() and not force:
        logger.error(
            f"{GLOSSSEQ2POLISH_FILEPATH} already exists!. To override, set force=True"
        )
        return
    gloss_annotations = list(
        map(
            lambda dict_: GlossAnnotationRecord(**dict_),
            jsonlines.open(GLOSS_ANNOTATIONS_FPATH),
        )
    )
    polish_annotations = list(
        map(
            lambda dict_: PolishAnnotationRecord(**dict_),
            jsonlines.open(POLISH_ANNOTATIONS_FPATH),
        )
    )
    with jsonlines.open(GLOSSSEQ2POLISH_FILEPATH, mode="w") as writer:
        for polish_annotation in callback(polish_annotations, **kwargs):
            gloss_annotations_for_polish = collect_gloss_annotations(
                polish_annotation, gloss_annotations
            )
            if any(gloss_annotations_for_polish):
                record_dto = GlossSeq2PolishRecord(
                    gloss_sequence=gloss_annotations_for_polish,
                    polish_annotation=polish_annotation,
                )
                writer.write(record_dto.model_dump())
