from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class State(Enum):
    """Ontological states for an agent."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Emotions:
    """Representation of basic emotions."""

    fear: float = 0.0
    joy: float = 0.0
    anger: float = 0.0

    def intensity(self) -> float:
        """Return the highest emotional intensity."""
        return max(self.fear, self.joy, self.anger)


@dataclass
class Agent:
    """Ontological agent capable of changing philosophical states."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotions: Emotions = field(default_factory=Emotions)
    history: List[State] = field(default_factory=lambda: [State.EGO])

    def feel(self, **kwargs: float) -> None:
        """Update emotions and adjust tension accordingly."""
        for emotion, value in kwargs.items():
            if hasattr(self.emotions, emotion):
                setattr(self.emotions, emotion, value)
        self.tension = max(self.tension, self.emotions.intensity())

    def update_state(self) -> None:
        """Transition to the next state if thresholds are exceeded."""
        triggered = self.tension > 0.7 or self.emotions.intensity() > 0.5
        if self.state == State.EGO and triggered:
            self.state = State.JAZ
        elif self.state == State.JAZ and triggered:
            self.state = State.ENOTNOST
        self.history.append(self.state)

    def respond(self, question: str = "") -> str:
        """Respond according to the current philosophical stance."""
        if self.state == State.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == State.JAZ:
            return "Resnica je relativna in oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
