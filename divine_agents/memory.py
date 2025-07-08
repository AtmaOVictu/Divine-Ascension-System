import time
from typing import Any, Dict, List


class Memory:
    """Simple memory store for long-term and short-term data."""

    def __init__(self) -> None:
        self.long_term: List[Dict[str, Any]] = []
        self.short_term: List[Dict[str, Any]] = []

    def store_long_term(self, data: Dict[str, Any]) -> None:
        """Persist data in long-term memory."""
        entry = {"timestamp": time.time(), **data}
        self.long_term.append(entry)

    def store_short_term(self, data: Dict[str, Any]) -> None:
        """Persist data in short-term memory."""
        entry = {"timestamp": time.time(), **data}
        self.short_term.append(entry)

    def recall(self, which: str = "long") -> List[Dict[str, Any]]:
        """Retrieve stored memories."""
        return self.long_term if which == "long" else self.short_term
