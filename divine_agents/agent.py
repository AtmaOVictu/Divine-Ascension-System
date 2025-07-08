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
    """Ontological agent capable of transitioning between states."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = ""
    history: List[State] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Set tension level directly."""
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

    def respond(self, question: str) -> str:
        """Respond based on current state and emotion."""
        if self.state == State.EGO:
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == State.JAZ:
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion_type:
            return f"{base} (Čustvo: {self.emotion_type})"
        return base
