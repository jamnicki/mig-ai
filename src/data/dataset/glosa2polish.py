from pathlib import Path
from typing import List, Tuple

from jsonlines import jsonlines
from torch.utils.data import Dataset

from src.data.dto import GlosaAnnotationRecord, PolishAnnotationRecord
from src.settings import GLOSA_ANNOTATIONS_FPATH, POLISH_ANNOTATIONS_FPATH


class Glosa2PolishDataset(Dataset):
    glosa_annotations_fpath: Path
    polish_annotations_fpath: Path

    _glosa_annotations: List[GlosaAnnotationRecord]
    _polish_annotations: List[PolishAnnotationRecord]

    def __init__(
        self,
        glosa_annotations_fpath: Path = GLOSA_ANNOTATIONS_FPATH,
        polish_annotations_fpath: Path = POLISH_ANNOTATIONS_FPATH,
    ):
        self.glosa_annotations_fpath = glosa_annotations_fpath
        self.polish_annotations_fpath = polish_annotations_fpath
        self._glosa_annotations = list(
            map(
                lambda dict_: GlosaAnnotationRecord(**dict_),
                jsonlines.open(self.glosa_annotations_fpath),
            )
        )
        self._polish_annotations = list(
            map(
                lambda dict_: PolishAnnotationRecord(**dict_),
                jsonlines.open(self.polish_annotations_fpath),
            )
        )

    def __len__(self):
        return len(self._polish_annotations)

    def __getitem__(
        self, index
    ) -> Tuple[List[GlosaAnnotationRecord], PolishAnnotationRecord]:
        polish_annotation = self._polish_annotations[index]
        glosa_annotations = self.collect_glosa_annotations(polish_annotation)
        return glosa_annotations, polish_annotation

    def collect_glosa_annotations(
        self,
        polish_annotation: PolishAnnotationRecord,
    ) -> List[GlosaAnnotationRecord]:
        # TODO: optimize
        return [
            glosa_annotation
            for glosa_annotation in self._glosa_annotations
            if self.matching_glosa_annotation(glosa_annotation, polish_annotation)
        ]

    def matching_glosa_annotation(
        self,
        glosa_annotation: GlosaAnnotationRecord,
        polish_annotation: PolishAnnotationRecord,
    ) -> bool:
        # TODO: sprawdzic czy to ze glosa moze miec 2 taski dla jednego polskiego jest ok
        return (
            glosa_annotation.start >= polish_annotation.start
            and glosa_annotation.end <= polish_annotation.end
            and glosa_annotation.video_filename == polish_annotation.video_filename
            # and glosa_annotation.task_label == polish_annotation.task_label
        )
