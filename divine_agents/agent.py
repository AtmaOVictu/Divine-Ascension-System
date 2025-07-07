"""Core agent logic used throughout the project."""

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class OntologicalState(Enum):
    """Enumeration of the possible ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = OntologicalState.EGO.value
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: [OntologicalState.EGO.value])

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # emotions build tension in the system
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == OntologicalState.EGO.value:
                self.state = OntologicalState.JAZ.value
            elif self.state == OntologicalState.JAZ.value:
                self.state = OntologicalState.ENOTNOST.value

        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""

        base = {
            OntologicalState.EGO.value: "Resnica je absolutna in neodvisna od drugih.",
            OntologicalState.JAZ.value: "Resnica je relativna, oblikovana z našimi odnosi.",
            OntologicalState.ENOTNOST.value: "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        # The more intense the emotion, the more emphatic the statement becomes.
        if self.emotion > 0.7:
            return f"{base} Čutim to zelo močno."
        if self.emotion > 0.3:
            return f"{base} V meni se prebuja čustven odziv."
        return base
