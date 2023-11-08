from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import jsonlines
from pathlib import Path

from src.settings import MERGED_MOVIES_DIR, GLOSS_ANNOTATIONS_FPATH, MOVIE_CLIPS_DIR
from src.data.dto import GlossAnnotationRecord


def video_slicer(input_path: str, output_path: str, start_time: int, end_time: int):
    ffmpeg_extract_subclip(
        input_path, start_time / 1000, end_time / 1000, targetname=output_path
    )


def list_video_slicer(movies_path):
    movie_list = []
    for file_path in movies_path.iterdir():
        if file_path.is_file():
            movie_list.append(file_path.name)

    with jsonlines.open(GLOSS_ANNOTATIONS_FPATH, mode="r") as file:
        for line in file:
            if line["video_filename"] not in movie_list:
                continue
            file_path = os.path.join(MERGED_MOVIES_DIR, line["video_filename"])
            annotation_desc = GlossAnnotationRecord(**line)

            save_path = (
                Path(MOVIE_CLIPS_DIR) / annotation_desc.video_filename.split(".")[0]
            )
            save_path.mkdir(parents=True, exist_ok=True)

            filename_path = (
                annotation_desc.video_filename.split(".")[0]
                + "__"
                + annotation_desc.task_label
                + "_"
                + str(annotation_desc.start)
                + "-"
                + str(annotation_desc.end)
                + ".mp4"
            )
            video_slicer(
                input_path=file_path,
                output_path=save_path / filename_path,
                start_time=annotation_desc.start,
                end_time=annotation_desc.end,
            )


if __name__ == "__main__":
    list_video_slicer(MERGED_MOVIES_DIR)
