from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .states import State, philosophy_response


@dataclass
class Agent:
    """Ontological agent capable of transitioning between states."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotion: float = 0.0
    history: List[State] = field(default_factory=lambda: [State.EGO])

    TENSION_THRESHOLD: float = 0.7
    EMOTION_THRESHOLD: float = 0.5

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition_if_needed(self) -> bool:
        """Perform state transition if thresholds are exceeded."""
        transitioned = False
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
            if self.state == State.EGO:
                self.state = State.JAZ
                transitioned = True
            elif self.state == State.JAZ:
                self.state = State.ENOTNOST
                transitioned = True
        if transitioned:
            self.history.append(self.state)
        return transitioned

    def respond(self, _question: str) -> str:
        """Return a philosophical statement based on current state."""
        return philosophy_response(self.state)
