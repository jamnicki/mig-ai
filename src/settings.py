from pathlib import Path


def get_project_root() -> Path:
    import git

    return Path(git.Repo(".", search_parent_directories=True).working_tree_dir)  # type: ignore


ROOT = get_project_root()
DATA_DIR = ROOT / "data"

ORKPJM_DIR = DATA_DIR / "ORKPJM"
ORKPJM_VIDEOS_DIR = ORKPJM_DIR / "filmy_ORKPJM"
ORKPJM_ANN_DIR = ORKPJM_DIR / "eafy_ORKPJM"
