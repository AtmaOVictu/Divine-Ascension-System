from dataclasses import dataclass, field
from typing import List


@dataclass
class Emotions:
    """Container for an agent's emotional state."""

    fear: float = 0.0
    joy: float = 0.0
    anger: float = 0.0

    def intensity(self) -> float:
        """Return the highest emotional intensity."""
        return max(self.fear, self.joy, self.anger)


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: Emotions | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions if emotions is not None else Emotions()
        self.history: List[str] = [state]

    def feel(self, **kwargs: float) -> None:
        """Update emotional state and adjust tension."""
        for emotion, value in kwargs.items():
            if hasattr(self.emotions, emotion):
                setattr(self.emotions, emotion, value)
        self.tension = max(self.tension, self.emotions.intensity())

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        triggered = self.tension > 0.7 or self.emotions.intensity() > 0.5
        if self.state == "Ego" and triggered:
            self.state = "Jaz"
        elif self.state == "Jaz" and triggered:
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
