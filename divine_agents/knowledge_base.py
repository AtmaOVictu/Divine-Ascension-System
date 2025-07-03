"""Simple knowledge base used by the agent system."""
from __future__ import annotations

import copy
from typing import Any, Dict, List


class KnowledgeBase:
    """Store reusable components for agents and modules."""

    def __init__(self) -> None:
        self.library: Dict[str, List[str]] = {
            "nujnosti": ["nova naloga", "krična napaka", "sprememba stanja"],
            "naloge": ["samospoznanje", "logični prehod", "emotivni prehod"],
            "agenti": ["Agent1", "Agent2", "Agent3"],
            "prehodi": ["samospoznanje", "logični prehod", "emotivni prehod"],
        }

    def print_from_library(self, category: str) -> None:
        """Print components from the requested category."""
        if category in self.library:
            print(f"Komponente v kategoriji '{category}': {self.library[category]}")
        else:
            print(f"Kategorija '{category}' ni najdena v bazi znanja.")

    def copy_from_library(self, category: str) -> List[str]:
        """Return a copy of components from the library for a given category."""
        if category in self.library:
            return copy.deepcopy(self.library[category])
        print(f"Kategorija '{category}' ni najdena v bazi znanja.")
        return []
