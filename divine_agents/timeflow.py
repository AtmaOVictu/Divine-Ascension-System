from dataclasses import dataclass
from typing import List, Optional


@dataclass
class AbsoluteDefinition:
    """Represents an absolute definition at a specific timestamp."""
    name: str
    value: str
    timestamp: str


class TimeFlow:
    """Stores absolute definitions over time."""

    def __init__(self) -> None:
        self.history: List[AbsoluteDefinition] = []

    def add_absolute(self, absolute: AbsoluteDefinition) -> None:
        self.history.append(absolute)

    def latest(self) -> Optional[AbsoluteDefinition]:
        return self.history[-1] if self.history else None

