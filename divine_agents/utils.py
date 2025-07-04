"""Utility functions for file system access and history logging."""

from __future__ import annotations

import datetime
import os
from typing import List


def access_local_disk(path: str) -> List[str]:
    """Return a list of entries in the given directory if it exists."""
    if os.path.exists(path):
        return os.listdir(path)
    raise FileNotFoundError(f"Pot {path} ne obstaja.")


def log_history(action: str, path: str = "history_log.txt") -> None:
    """Append an action with timestamp to the history log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {action}\n"
    with open(path, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

