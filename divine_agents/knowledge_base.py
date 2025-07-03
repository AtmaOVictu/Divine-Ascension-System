from __future__ import annotations

"""Module providing a simple knowledge base for agents."""

from copy import deepcopy
from typing import Dict, List


class KnowledgeBase:
    """Represents a repository of known components for agents."""

    def __init__(self) -> None:
        self.library: Dict[str, List[str]] = {
            "nujnosti": ["nova naloga", "kritična napaka", "sprememba stanja"],
            "naloge": ["samospoznanje", "logični prehod", "emotivni prehod"],
            "agenti": ["Agent1", "Agent2", "Agent3"],
            "prehodi": ["samospoznanje", "logični prehod", "emotivni prehod"],
        }

    def print_from_library(self, category: str) -> str:
        """Return a formatted string of components for the given category."""
        if category not in self.library:
            raise KeyError(f"Kategorija '{category}' ni najdena v bazi znanja.")
        items = self.library[category]
        return f"Komponente v kategoriji '{category}': {items}"

    def copy_from_library(self, category: str) -> List[str]:
        """Return a deep copy of the components for the given category."""
        if category not in self.library:
            raise KeyError(f"Kategorija '{category}' ni najdena v bazi znanja.")
        return deepcopy(self.library[category])
