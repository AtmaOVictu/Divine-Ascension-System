"""Agent model for ontological state transitions and responses."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class State(Enum):
    """Enumeration of the possible ontological states."""

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
    history: List[State] = field(default_factory=lambda: [State.EGO])

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and propagate to tension."""

        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set the tension level directly."""

        self.tension = value

    def transition(self) -> State:
        """Transition to the next state if thresholds are exceeded."""

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == State.EGO:
                self.state = State.JAZ
            elif self.state == State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, _: str) -> str:
        """Return a philosophical statement based on the current state."""

        if self.state == State.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == State.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

