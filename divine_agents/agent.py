from dataclasses import dataclass, field
from typing import List

from .states import EGO, JAZ, ENOTNOST, OntologicalState


@dataclass
class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    name: str
    state: OntologicalState = EGO
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: [EGO.name])

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == EGO:
                self.state = JAZ
            elif self.state == JAZ:
                self.state = ENOTNOST
        self.history.append(self.state.name)
        return self.state.name

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        return self.state.principle
