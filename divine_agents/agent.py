"""Core functionality for ontological agents."""

from enum import Enum


class EmotionType(Enum):
    """Enumerates possible emotional tones for an agent."""

    NEUTRAL = "neutral"
    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: EmotionType = EmotionType.NEUTRAL):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: EmotionType = EmotionType.NEUTRAL) -> None:
        """Update emotion intensity and adjust tension and tone."""
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value

    def _emotion_prefix(self) -> str:
        """Return a short textual prefix representing the emotional tone."""
        if self.emotion_type == EmotionType.FEAR:
            return "V strahu, "
        if self.emotion_type == EmotionType.JOY:
            return "Z veseljem, "
        if self.emotion_type == EmotionType.ANGER:
            return "Z jezo, "
        return ""

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
        prefix = self._emotion_prefix()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{base}"
