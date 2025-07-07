"""Ontological agent capable of emotional state transitions and responses."""

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class OntologicalState(Enum):
    """Possible ontological states for an agent."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represents an agent with tension and emotional state."""

    name: str
    state: OntologicalState = OntologicalState.EGO
    tension: float = 0.0
    emotion_intensity: float = 0.0
    emotion_type: str = "neutral"
    history: List[OntologicalState] = field(default_factory=lambda: [OntologicalState.EGO])

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""

        self.emotion_type = emotion_type
        self.emotion_intensity = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""

        self.tension = value

    def transition(self) -> OntologicalState:
        """Perform state transition if thresholds are exceeded."""

        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == OntologicalState.EGO:
                self.state = OntologicalState.JAZ
            elif self.state == OntologicalState.JAZ:
                self.state = OntologicalState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""

        prefix = f"[{self.emotion_type}] " if self.emotion_type != "neutral" else ""
        if self.state == OntologicalState.EGO:
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == OntologicalState.JAZ:
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."

