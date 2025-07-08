"""Ontological agents capable of state transitions and philosophical responses."""

from dataclasses import dataclass, field
from enum import Enum


class State(Enum):
    """Enumeration of possible ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represents an agent with emotional tension and ontological state."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotion: float = 0.0
    history: list[str] = field(default_factory=lambda: [State.EGO.value])

    def update_emotion(self, value: float) -> None:
        """Update emotional intensity and adjust tension accordingly."""
        self.emotion = max(0.0, value)
        self.tension = max(self.tension + value, 0.0)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, value)

    def transition(self) -> State:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state is State.EGO:
                self.state = State.JAZ
            elif self.state is State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state.value)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state."""
        if self.state is State.EGO:
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state is State.JAZ:
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            base += " Moji občutki to še okrepijo."  # emotional colour
        return base
