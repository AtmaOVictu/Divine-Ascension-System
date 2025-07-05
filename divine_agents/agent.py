from dataclasses import dataclass, field
from enum import Enum
from typing import List


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
    emotion: float = 0.0
    history: List[OntologicalState] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Initialize the history with the starting state."""
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
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
        if self.state == OntologicalState.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == OntologicalState.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
