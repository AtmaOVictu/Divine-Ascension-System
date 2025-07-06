"""Agent models an entity that transitions through ontological states."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class State(Enum):
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
            if self.state is State.EGO:
                self.state = State.JAZ
            elif self.state is State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""

        base: str
        if self.state is State.EGO:
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state is State.JAZ:
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            base += f" Čutim napetost {self.emotion:.2f}."
        return base

