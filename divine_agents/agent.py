from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List


class OntologicalState(Enum):
    """Enumeration of possible ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represent an ontological agent that can transition states."""

    name: str
    state: OntologicalState = OntologicalState.EGO
    tension: float = 0.0
    emotions: Dict[str, float] = field(default_factory=dict)
    history: List[OntologicalState] = field(default_factory=lambda: [OntologicalState.EGO])

    EMOTION_THRESHOLD: float = 0.5
    TENSION_THRESHOLD: float = 0.7

    def update_emotion(self, name: str, value: float) -> None:
        """Update a specific emotion and adjust tension."""
        self.emotions[name] = value
        self.tension += value

    def dominant_emotion(self) -> float:
        """Return the highest emotion intensity."""
        return max(self.emotions.values(), default=0.0)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> OntologicalState:
        """Transition to the next ontological state if thresholds are exceeded."""
        if self.tension > self.TENSION_THRESHOLD or self.dominant_emotion() > self.EMOTION_THRESHOLD:
            if self.state == OntologicalState.EGO:
                self.state = OntologicalState.JAZ
            elif self.state == OntologicalState.JAZ:
                self.state = OntologicalState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical statement based on the current state and emotion."""
        emotion_descriptor = ""
        dom_emotion = self.dominant_emotion()
        if dom_emotion > 0.5:
            emotion_descriptor = " (s čustvi)"

        if self.state == OntologicalState.EGO:
            return f"Resnica je absolutna in neodvisna od drugih.{emotion_descriptor}"
        if self.state == OntologicalState.JAZ:
            return f"Resnica je relativna, oblikovana z našimi odnosi.{emotion_descriptor}"
        return f"Vse resnice so eno, medsebojno povezane.{emotion_descriptor}"
