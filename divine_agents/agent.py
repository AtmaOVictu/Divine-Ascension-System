"""Ontological agents capable of evolving through philosophical states."""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Tuple


class OntologicalState(Enum):
    """Enumeration of possible agent states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represents an agent with emotional and ontological attributes."""

    name: str
    state: OntologicalState = OntologicalState.EGO
    tension: float = 0.0
    emotion: Optional[Tuple[str, float]] = None
    history: List[OntologicalState] = field(
        default_factory=lambda: [OntologicalState.EGO]
    )

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion = (emotion, intensity)
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        intensity = self.emotion[1] if self.emotion else 0.0
        if self.tension > 0.7 or intensity > 0.5:
            if self.state == OntologicalState.EGO:
                self.state = OntologicalState.JAZ
            elif self.state == OntologicalState.JAZ:
                self.state = OntologicalState.ENOTNOST
        self.history.append(self.state)
        return self.state.value

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotion."""
        responses = {
            OntologicalState.EGO: "Resnica je absolutna in neodvisna od drugih.",
            OntologicalState.JAZ: "Resnica je relativna, oblikovana z našimi odnosi.",
            OntologicalState.ENOTNOST: "Vse resnice so eno, medsebojno povezane.",
        }
        base = responses[self.state]
        if self.emotion and self.emotion[1] > 0.5:
            prefix = f"{self.emotion[0].capitalize()} vodi me do misli, da "
            return prefix + base.lower()
        return base
