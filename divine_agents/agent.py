"""Ontological agents and state management."""

from dataclasses import dataclass, field
from enum import Enum


class State(str, Enum):
    """Enumeration of possible ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotion: float = 0.0
    history: list = field(default_factory=list)

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> State:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == State.EGO:
                self.state = State.JAZ
            elif self.state == State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, _: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            State.EGO: "Resnica je absolutna in neodvisna od drugih.",
            State.JAZ: "Resnica je relativna, oblikovana z našimi odnosi.",
            State.ENOTNOST: "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotion > 0.5:
            return f"{base} (čustveni naboj: {self.emotion:.1f})"
        return base
