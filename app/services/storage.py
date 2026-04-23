import json
from pathlib import Path
from app.config.settings import SEEN_FILE_PATH

def load_seen_links() -> set:
    path = Path(SEEN_FILE_PATH)
    if not path.exists():
        return set()

    with open(path, "r", encoding="utf-8") as f:
        return set(json.load(f))


def save_seen_links(links: set):
    path = Path(SEEN_FILE_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(list(links), f, indent=2, ensure_ascii=False)
