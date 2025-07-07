"""Ontological agents that transition states based on emotion and tension."""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class OntologicalState(Enum):
    """Enumeration of possible ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: OntologicalState = OntologicalState.EGO
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion_type: Optional[str] = None
    history: List[OntologicalState] = field(default_factory=lambda: [OntologicalState.EGO])

    def update_emotion(self, value: float, emotion_type: Optional[str] = None) -> None:
        """Update emotion intensity and optionally set emotion type."""

        self.emotion_level = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""

        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""

        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == OntologicalState.EGO:
                self.state = OntologicalState.JAZ
            elif self.state == OntologicalState.JAZ:
                self.state = OntologicalState.ENOTNOST
        self.history.append(self.state)
        return self.state.value

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""

        if self.state == OntologicalState.EGO:
            base = "Truth is absolute and independent of others."
        elif self.state == OntologicalState.JAZ:
            base = "Truth is relative and shaped by our relationships."
        else:
            base = "All truths are one and interconnected."

        if self.emotion_type:
            base += f" Emotion: {self.emotion_type}."
        return base
