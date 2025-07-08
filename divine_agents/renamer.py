import os


class FileRenamingAgent:
    """Agent capable of renaming files on the filesystem."""

    def __init__(self, name: str):
        self.name = name

    def rename_file(self, current_file: str, new_file: str) -> bool:
        """Rename a file if it exists.

        Returns ``True`` when the rename succeeded and ``False`` otherwise.
        """
        if os.path.exists(current_file):
            os.rename(current_file, new_file)
            return True
        return False
