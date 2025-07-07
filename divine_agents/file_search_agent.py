from pathlib import Path
from .orchestrator import SubAgent


class FileSearchAgent(SubAgent):
    """Agent that searches for files matching a pattern."""

    def __init__(self, root: str, pattern: str = "*"):
        self.root = Path(root)
        self.pattern = pattern

    def is_relevant(self, input_data: str) -> bool:
        return "file" in input_data.lower() or "search" in input_data.lower()

    def process(self, input_data: str) -> str:
        matches = [str(p) for p in self.root.rglob(self.pattern)]
        return f"Found {len(matches)} files."
