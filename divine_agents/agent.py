from dataclasses import dataclass
from .emotion import Emotion


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion: Emotion = emotion or Emotion("neutral", 0.0)
        self.history = [state]

    def update_emotion(self, emotion: Emotion) -> None:
        """Update emotional state and adjust tension accordingly."""
        self.emotion = emotion
        self.tension += emotion.intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion.intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        prefix = (
            "" if self.emotion.kind == "neutral" else f"({self.emotion.kind}) "
        )
        if self.state == "Ego":
            return f"{prefix}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{prefix}Resnica je relativna, oblikovana z našimi odnosi."
        return f"{prefix}Vse resnice so eno, medsebojno povezane."
