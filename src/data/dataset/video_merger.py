from pathlib import Path
from moviepy.editor import VideoFileClip, clips_array, concatenate_videoclips


from src.settings import ORKPJM_VIDEOS_DIR, MERGED_MOVIES_DIR


def merge_videos(videos_path):
    files_dict = {}
    # Przejście po filmach w folderze i znajdowanie "grup"
    for file_path in videos_path.iterdir():
        if file_path.is_file() and file_path.suffix == ".mp4":
            file_name = file_path.stem
            prefix = file_name.split("_")[0]

            if prefix in files_dict:
                files_dict[prefix].append(file_path)
            else:
                files_dict[prefix] = [file_path]
                
    # Połączenie plików o tym samym przedrostku
    for prefix, file_paths in files_dict.items():
        if len(file_paths) > 1:
            clips = [VideoFileClip(str(file)) for file in file_paths]
            final_clip = concatenate_videoclips(clips)
            final_clip.write_videofile(
                str(MERGED_MOVIES_DIR / f"{prefix}.mp4"), codec="libx264", threads=4
            )

    print("Operacja zakończona.")


if __name__ == "__main__":
    merge_videos(ORKPJM_VIDEOS_DIR)
