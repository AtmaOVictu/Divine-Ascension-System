"""BoxingStation module for managing interactions between entities."""
from typing import Any, List

from .agent import Agent


class Bit:
    """Simple representation of a binary value."""

    def __init__(self, value: int):
        if value not in (0, 1):
            raise ValueError("Bit value must be 0 or 1.")
        self.value = value


class BoxingStation:
    """Create boxes when two entities interact."""

    def __init__(self) -> None:
        self.boxes: List[str] = []

    def create_box(self, box_name: str) -> None:
        """Add a new box representing an interaction outcome."""
        self.boxes.append(box_name)

    def interaction(self, entity1: Any, entity2: Any) -> str | None:
        """Generate a box depending on interacting entities."""
        if isinstance(entity1, Agent) and isinstance(entity2, Agent):
            if entity1.state == "Ego" and entity2.state == "Jaz":
                self.create_box("Self-Other Reflection Box")
            elif entity1.state == "Jaz" and entity2.state == "Enotnost":
                self.create_box("Unity Reflection Box")
        elif isinstance(entity1, Bit) and isinstance(entity2, Bit):
            if entity1.value == 0 and entity2.value == 1:
                self.create_box("Bit Interaction Box")
        return self.boxes[-1] if self.boxes else None
