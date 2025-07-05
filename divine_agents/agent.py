"""Ontological agents capable of philosophical state transitions."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple


class State(Enum):
    """Possible ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Emotions:
    """Container for agent emotions."""

    fear: float = 0.0
    joy: float = 0.0
    anger: float = 0.0

    def intensity(self) -> float:
        """Return the maximum emotional intensity."""
        return max(self.fear, self.joy, self.anger)


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    def __init__(
        self,
        name: str,
        state: State | str = State.EGO,
        tension: float = 0.0,
        emotions: Emotions | None = None,
    ) -> None:
        self.name = name
        self.state = State(state) if isinstance(state, str) else state
        self.tension = tension
        self.emotions = emotions or Emotions()
        self.history: List[Tuple[State, float]] = [(self.state, self.tension)]

    def update_emotion(self, value: float, emotion: str = "joy") -> None:
        """Update a specific emotion and adjust tension."""

        if hasattr(self.emotions, emotion):
            setattr(self.emotions, emotion, value)
        # tension reflects overall emotional intensity
        self.tension = max(self.tension, self.emotions.intensity())

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""

        self.tension = value

    def transition(self) -> State:
        """Perform a state transition if thresholds are exceeded."""

        if self.tension > 0.7 or self.emotions.intensity() > 0.5:
            if self.state is State.EGO:
                self.state = State.JAZ
            elif self.state is State.JAZ:
                self.state = State.ENOTNOST
        self.history.append((self.state, self.tension))
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current state."""

        if self.state is State.EGO:
            return f"{self.name}: Resnica je absolutna in neodvisna od drugih."
        if self.state is State.JAZ:
            return f"{self.name}: Resnica je relativna, oblikovana z našimi odnosi."
        return f"{self.name}: Vse resnice so eno, medsebojno povezane."

