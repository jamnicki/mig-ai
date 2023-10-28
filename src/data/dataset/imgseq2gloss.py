from pathlib import Path
from typing import List

from jsonlines import jsonlines
from torch.utils.data import Dataset

from src.data.dto import ImgSeq2GlossRecord
from src.settings import IMGSEQ2GLOSS_FILEPATH


class ImgSeq2Gloss(Dataset):
    data_records: List[ImgSeq2GlossRecord]
    data_fpath: Path

    def __init__(
        self,
        data_fpath: Path = IMGSEQ2GLOSS_FILEPATH,
    ):
        self.data_fpath = data_fpath
        self.data_records = list(
            map(ImgSeq2GlossRecord.from_dict, jsonlines.open(self.data_fpath))
        )

    def __len__(self):
        return len(self.data_records)

    def __getitem__(self, index) -> ImgSeq2GlossRecord:
        return self.data_records[index]
