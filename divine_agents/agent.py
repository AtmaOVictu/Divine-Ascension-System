"""Core agent classes used for philosophical simulations."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Emotion:
    """Represents an emotional state with a name and intensity."""

    name: str
    intensity: float


class Agent:
    """An ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Optional[Emotion] = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion: Optional[Emotion] = emotion
        self.history = [state]

    def update_emotion(self, value: float, name: Optional[str] = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = Emotion(name or (self.emotion.name if self.emotion else ""), value)
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        intensity = self.emotion.intensity if isinstance(self.emotion, Emotion) else 0
        if self.tension > 0.7 or intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        prefix = f"[{self.emotion.name}] " if isinstance(self.emotion, Emotion) and self.emotion.name else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
