from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .state import OntoState


@dataclass
class Agent:
    """Ontological agent that transitions between states based on emotion and tension."""

    name: str
    state: OntoState = OntoState.EGO
    tension: float = 0.0
    emotion: float = 0.0
    history: List[OntoState] = field(default_factory=lambda: [OntoState.EGO])

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> OntoState:
        """Transition to the next ontological state if thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state is OntoState.EGO:
                self.state = OntoState.JAZ
            elif self.state is OntoState.JAZ:
                self.state = OntoState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer reflecting the current state."""
        return self.state.philosophy()
