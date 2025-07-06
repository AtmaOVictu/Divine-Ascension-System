"""Ontological agent implementation used in tests and simulations."""

from dataclasses import dataclass
from typing import List


@dataclass
class Emotion:
    """Simple container describing an emotion and its intensity."""

    name: str
    level: float


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = float(tension)
        self.emotion: Emotion = emotion or Emotion("neutral", 0.0)
        self.history: List[str] = [state]

    def update_emotion(self, name: str, level: float) -> None:
        """Update emotion information and adjust tension accordingly."""
        self.emotion = Emotion(name, level)
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = float(value)

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion.level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (čustvo: {self.emotion.name})"
