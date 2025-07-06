from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class OntologicalState(str, Enum):
    """Enum representing the philosophical states an agent can occupy."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: OntologicalState = OntologicalState.EGO
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: Optional[str] = None
    history: List[OntologicalState] = field(default_factory=lambda: [OntologicalState.EGO])

    def update_emotion(self, value: float, kind: Optional[str] = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if kind:
            self.emotion_type = kind
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> OntologicalState:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == OntologicalState.EGO:
                self.state = OntologicalState.JAZ
            elif self.state == OntologicalState.JAZ:
                self.state = OntologicalState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            OntologicalState.EGO: "Resnica je absolutna in neodvisna od drugih.",
            OntologicalState.JAZ: "Resnica je relativna, oblikovana z našimi odnosi.",
            OntologicalState.ENOTNOST: "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotion_type:
            return f"{base} (občutek: {self.emotion_type})"
        return base
