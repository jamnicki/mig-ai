from pathlib import Path


def get_project_root() -> Path:
    import git

    return Path(git.Repo(".", search_parent_directories=True).working_tree_dir)  # type: ignore


ROOT = get_project_root()
DATA_DIR = ROOT / "data"

ORKPJM_DIR = DATA_DIR / "ORKPJM"
ORKPJM_VIDEOS_DIR = ORKPJM_DIR / "filmy_korpus"
ORKPJM_ANN_DIR = ORKPJM_DIR / "eafy_CZERWIEC2021"

PREPROCESSED_DIR = DATA_DIR / "preprocessed"
MERGED_MOVIES_DIR = PREPROCESSED_DIR / "merged_movies"
MOVIE_CLIPS_DIR = PREPROCESSED_DIR / "movie_clips"
PREPRO_ANNOTATIONS_DIR = PREPROCESSED_DIR / "annotations"
GLOSS_ANNOTATIONS_FPATH = PREPRO_ANNOTATIONS_DIR / "glosa_annotations.jsonl"
POLISH_ANNOTATIONS_FPATH = PREPRO_ANNOTATIONS_DIR / "polish_annotations.jsonl"
POLISH_ANNOTATIONS_SLICED = PREPROCESSED_DIR / "polish_anotations_sliced"

GLOSSSEQ2POLISH_FILEPATH = PREPROCESSED_DIR / "glossseq2polish.jsonl"
IMGSEQ2GLOSS_FILEPATH = PREPROCESSED_DIR / "imgseq2gloss.jsonl"

TASK_LABELS = ["07", "08", "13", "15", "17", "24"]
TASK_LABEL_NAME_MAP = {
    "07": "Kalendarz",
    "08": "Sylwester / Żaba",
    "13": "Komisky",
    "15": "Znaki zakazu",
    "17": "Gruszki / Chaplin",
    "24": "Alarm",
}

GLOSS_SPECIAL_SYMBOLS = ["###", "^", "%", "&", "@"]
GLOSS_ADDITIONAL_ABBR = [
    "IDENTYF:",
    "$:KL:",
    "WSKAZ:",
    "G:",
]
