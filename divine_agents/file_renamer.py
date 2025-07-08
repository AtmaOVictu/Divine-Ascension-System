import os

class FileRenamingAgent:
    """Agent capable of renaming Python files dynamically."""

    def __init__(self, name: str):
        self.name = name

    def rename_file(self, current: str, new: str) -> bool:
        """Rename a file if it exists. Returns True on success."""
        if not os.path.exists(current):
            return False
        try:
            os.rename(current, new)
            return True
        except OSError:
            return False
