"""Ontological agents capable of moving between philosophical states."""

from enum import Enum
from typing import Optional


class Emotion(Enum):
    """Simple enumeration of basic emotions."""

    NEUTRAL = "neutral"
    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion_level: float = 0.0,
        emotion_type: Emotion = Emotion.NEUTRAL,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion_level
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion: Emotion) -> None:
        """Update emotion intensity and type, adjusting tension."""
        self.emotion = value
        self.emotion_type = emotion
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type != Emotion.NEUTRAL:
            base += f" Čutim {self.emotion_type.value}."
        return base
