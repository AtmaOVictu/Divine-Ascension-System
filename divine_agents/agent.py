from enum import Enum


class Emotion(Enum):
    """Supported emotional states influencing transitions."""

    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"
    NEUTRAL = "neutral"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        current_emotion: Emotion | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.current_emotion = current_emotion or Emotion.NEUTRAL
        self.history = [state]

    def update_emotion(self, value: float, kind: Emotion | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.current_emotion = kind or self.current_emotion
        if self.current_emotion in (Emotion.FEAR, Emotion.ANGER):
            self.tension = min(1.0, self.tension + value)
        elif self.current_emotion == Emotion.JOY:
            self.tension = max(0.0, self.tension - value / 2)
        else:
            self.tension = min(1.0, self.tension + value / 2)

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
        suffix = "!" if self.emotion > 0.5 else "."
        if self.state == "Ego":
            text = "Resnica je absolutna in neodvisna od drugih"
        elif self.state == "Jaz":
            text = "Resnica je relativna, oblikovana z našimi odnosi"
        else:
            text = "Vse resnice so eno, medsebojno povezane"
        return f"{text}{suffix}"
