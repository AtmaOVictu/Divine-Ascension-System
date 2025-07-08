from dataclasses import dataclass
from typing import Optional


@dataclass
class Emotion:
    """Simple representation of an emotional state."""

    name: str
    intensity: float


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: Optional[Emotion] = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, name: str, intensity: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion = Emotion(name, intensity)
        self.tension += intensity

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
        emotion_note = (
            f" Občutim {self.emotion.name}." if self.emotion else ""
        )
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + emotion_note
        if self.state == "Jaz":
            return (
                "Resnica je relativna, oblikovana z našimi odnosi." + emotion_note
            )
        return "Vse resnice so eno, medsebojno povezane." + emotion_note
