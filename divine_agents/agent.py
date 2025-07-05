from typing import Optional

from .emotion import Emotion


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: Optional[Emotion] = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion("neutral", 0.0)
        self.history = [state]

    def update_emotion(self, name: str, intensity: float) -> None:
        """Update emotion type and intensity, adjusting tension accordingly."""
        self.emotion = Emotion(name, intensity)
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        intensity = self.emotion.intensity
        if self.tension > 0.7 or intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotion.intensity > 0.5:
            return f"{base} (občutim {self.emotion.name})"
        return base

