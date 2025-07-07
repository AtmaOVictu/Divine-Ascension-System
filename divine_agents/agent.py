from dataclasses import dataclass
from typing import Optional


@dataclass
class Emotion:
    """Represents an emotion affecting the agent."""

    name: str
    intensity: float


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Optional[Emotion] = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion: Optional[Emotion] = emotion
        self.history = [state]

    def update_emotion(self, value: float, kind: Optional[str] = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = Emotion(kind or "", value)
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        intensity = self.emotion.intensity if self.emotion else 0.0
        if self.tension > 0.7 or intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = ""
        if self.emotion and self.emotion.name:
            prefix = f"[Obcutek: {self.emotion.name}] "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z nasimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
