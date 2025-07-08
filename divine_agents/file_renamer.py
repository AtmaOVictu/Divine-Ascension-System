import os
from pathlib import Path


class FileRenamingAgent:
    """Agent that can rename Python files within the system."""

    def __init__(self, name: str):
        self.name = name

    def rename_file(self, current: str, new: str) -> bool:
        """Rename a file and return True on success."""
        current_path = Path(current)
        if not current_path.exists():
            return False
        try:
            os.rename(current, new)
            return True
        except OSError:
            return False
