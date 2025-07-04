import datetime
import os


def access_local_disk(path: str):
    """Return list of files in a directory or raise if it doesn't exist."""
    if os.path.exists(path):
        return os.listdir(path)
    raise FileNotFoundError(f"Pot {path} ne obstaja.")


def log_history(action: str, path: str = "history_log.txt") -> None:
    """Append an action with timestamp to a log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} - {action}\n"
    with open(path, "a", encoding="utf-8") as log_file:
        log_file.write(entry)
