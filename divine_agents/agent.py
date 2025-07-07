"""Ontological agent implementation."""

from enum import Enum
from typing import List


class OntologicalState(Enum):
    """Enumeration of ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = (
        OntologicalState.EGO,
        OntologicalState.JAZ,
        OntologicalState.ENOTNOST,
    )

    def __init__(
        self,
        name: str,
        state: OntologicalState | str = OntologicalState.EGO,
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
        self.name = name
        self.state = (
            OntologicalState(state) if isinstance(state, str) else state
        )
        self.tension = tension
        self.emotion = emotion
        self.history: List[OntologicalState] = [self.state]
        self.potential_changes: List[str] = []

    def record_potential_change(self, change: str) -> None:
        """Record a change in hexadecimal form for hexdump-like tracking."""
        self.potential_changes.append(change.encode().hex())

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.record_potential_change(f"emotion:{value}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.record_potential_change(f"tension:{value}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == OntologicalState.EGO:
                self.state = OntologicalState.JAZ
            elif self.state == OntologicalState.JAZ:
                self.state = OntologicalState.ENOTNOST
            self.record_potential_change(f"state:{self.state.value}")
        self.history.append(self.state)
        return self.state.value

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emph = "!" if self.emotion > 0.5 else "."
        if self.state == OntologicalState.EGO:
            return f"Resnica je absolutna in neodvisna od drugih{emph}"
        if self.state == OntologicalState.JAZ:
            return f"Resnica je relativna, oblikovana z našimi odnosi{emph}"
        return f"Vse resnice so eno, medsebojno povezane{emph}"
