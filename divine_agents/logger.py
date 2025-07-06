import json
import time
from typing import List, Dict, Optional

class ChangeLogger:
    """Simple logger that stores agent changes for analysis."""

    def __init__(self, file_name: Optional[str] = None):
        self.file_name = file_name
        self.changes: List[Dict] = []
        if self.file_name:
            try:
                with open(self.file_name, "r", encoding="utf-8") as f:
                    self.changes = json.load(f)
            except FileNotFoundError:
                self.changes = []

    def log(self, change_type: str, description: str, data: Dict, status: str = "active") -> None:
        entry = {
            "type": change_type,
            "description": description,
            "data": data,
            "status": status,
            "timestamp": time.time(),
        }
        self.changes.append(entry)
        self.save()

    def save(self) -> None:
        if not self.file_name:
            return
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(self.changes, f, indent=2)

    def get_changes(self, status: Optional[str] = None) -> List[Dict]:
        if status:
            return [c for c in self.changes if c.get("status") == status]
        return list(self.changes)
