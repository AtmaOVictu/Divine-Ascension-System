"""Core primitives for modelling ontological agents."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class State(Enum):
    """Possible ontological states for an agent."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represents an agent capable of changing ontological states."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotion: float = 0.0
    history: List[State] = field(default_factory=lambda: [State.EGO])

    TRANSITION_TENSION: float = 0.7
    TRANSITION_EMOTION: float = 0.5

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> State:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.TRANSITION_TENSION or self.emotion > self.TRANSITION_EMOTION:
            if self.state == State.EGO:
                self.state = State.JAZ
            elif self.state == State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == State.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == State.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
