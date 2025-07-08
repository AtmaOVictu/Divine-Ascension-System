from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class OntologyState(Enum):
    """Possible ontological states for an agent."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Box:
    """Represents a box created when extremes are reached."""

    name: str


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    def __init__(
        self,
        name: str,
        state: OntologyState = OntologyState.EGO,
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = self._clamp(tension)
        self.emotion = self._clamp(emotion)
        self.history: List[OntologyState] = [state]
        self.new_boxes: List[Box] = []

    @staticmethod
    def _clamp(value: float) -> float:
        """Clamp a float to the 0..1 range."""
        return max(0.0, min(1.0, value))

    def _check_extremes(self) -> None:
        """Create new boxes if extreme values are reached."""
        if self.tension > 0.8:
            self.create_new_box("High Tension Box")
        if self.tension < 0.2:
            self.create_new_box("Low Tension Box")
        if self.emotion > 0.8:
            self.create_new_box("Extreme Emotion Box")
        if self.emotion < 0.2:
            self.create_new_box("Calm Emotion Box")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = self._clamp(value)
        self.tension = self._clamp(self.tension + self.emotion)
        self._check_extremes()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = self._clamp(value)
        self._check_extremes()

    def transition(self) -> OntologyState:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == OntologyState.EGO:
                self.state = OntologyState.JAZ
            elif self.state == OntologyState.JAZ:
                self.state = OntologyState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == OntologyState.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == OntologyState.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def create_new_box(self, name: str) -> None:
        """Record a newly created box."""
        self.new_boxes.append(Box(name))
