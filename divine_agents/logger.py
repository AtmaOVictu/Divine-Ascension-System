import json
import time
from typing import List, Dict, Any


class ChangeLogger:
    """Log and persist changes for later analysis."""

    def __init__(self, file_name: str | None = None):
        self.file_name = file_name
        self.changes: List[Dict[str, Any]] = []
        if self.file_name:
            try:
                with open(self.file_name, "r", encoding="utf-8") as file:
                    self.changes = json.load(file)
            except FileNotFoundError:
                self.changes = []

    def log_change(self, change_type: str, description: str, data: Any, status: str = "active") -> None:
        change = {
            "type": change_type,
            "description": description,
            "data": data,
            "status": status,
            "timestamp": time.time(),
        }
        self.changes.append(change)
        self.save_changes()

    def save_changes(self) -> None:
        if self.file_name:
            with open(self.file_name, "w", encoding="utf-8") as file:
                json.dump(self.changes, file, indent=4)

    def get_changes(self) -> List[Dict[str, Any]]:
        return list(self.changes)

    def get_active_changes(self) -> List[Dict[str, Any]]:
        return [c for c in self.changes if c["status"] == "active"]

    def get_lost_changes(self) -> List[Dict[str, Any]]:
        return [c for c in self.changes if c["status"] == "lost"]

    def archive_change(self, index: int) -> None:
        if 0 <= index < len(self.changes):
            self.changes[index]["status"] = "archived"
            self.save_changes()
