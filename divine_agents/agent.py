from typing import Optional

from .emotion import Emotion


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion_intensity: float = 0.0, emotion_name: str = "Nevtralno"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = Emotion(emotion_name, emotion_intensity)
        self.history = [state]

    def update_emotion(self, value: float, name: Optional[str] = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        if name:
            self.emotion.name = name
        self.emotion.intensity = value
        self.tension += value

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
