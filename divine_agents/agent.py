from __future__ import annotations

from enum import Enum, auto


class OntologyState(Enum):
    """Enumeration of ontological states represented with symbols."""

    EGO = "Ε"
    JAZ = "Ψ"
    ENOTNOST = "Ω"

    def next(self) -> "OntologyState":
        """Return the next ontological state in the cycle."""
        mapping = {
            OntologyState.EGO: OntologyState.JAZ,
            OntologyState.JAZ: OntologyState.ENOTNOST,
            OntologyState.ENOTNOST: OntologyState.ENOTNOST,
        }
        return mapping[self]


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
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> OntologyState:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            self.state = self.state.next()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == OntologyState.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == OntologyState.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def __str__(self) -> str:
        return f"{self.name} ({self.state.value}): Tension={self.tension}, Emotion={self.emotion}"
