import json
import time
from typing import List, Dict


class ChangeLogger:
    """Keep track of all agent changes and store them in a JSON file."""

    def __init__(self, file_name: str = "change_log.json"):
        self.file_name = file_name
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                self.changes: List[Dict] = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.changes = []

    def log_change(
        self,
        change_type: str,
        description: str,
        data: Dict,
        status: str = "active",
    ) -> None:
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
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.changes, file, indent=4)

    def get_changes(self) -> List[Dict]:
        return self.changes

    def get_active_changes(self) -> List[Dict]:
        return [ch for ch in self.changes if ch["status"] == "active"]

    def get_lost_changes(self) -> List[Dict]:
        return [ch for ch in self.changes if ch["status"] == "lost"]

    def archive_change(self, index: int) -> None:
        if 0 <= index < len(self.changes):
            self.changes[index]["status"] = "archived"
            self.save_changes()
