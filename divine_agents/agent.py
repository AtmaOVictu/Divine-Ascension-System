"""Core agent logic for the Divine-Ascension-System."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class State(str, Enum):
    """Enumeration of possible ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning between states."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotion: float = 0.0
    history: List[State] = field(default_factory=lambda: [State.EGO])

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

    def philosophy(self) -> str:
        """Return a philosophical statement for the current state."""
        if self.state == State.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == State.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return an answer influenced by current emotion and state."""
        base = self.philosophy()
        if self.emotion > 0.5:
            return f"({self.emotion:.1f}) {base}"
        return base
