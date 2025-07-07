from enum import Enum


class Emotion(Enum):
    """Possible emotional states influencing the agents."""

    FEAR = "strah"
    JOY = "veselje"
    ANGER = "jeza"
    NEUTRAL = "nevtralno"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: Emotion = Emotion.NEUTRAL):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: Emotion = Emotion.NEUTRAL) -> None:
        """Update emotion intensity, type and adjust tension accordingly."""
        self.emotion = value
        self.emotion_type = emotion_type
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
        """Return a philosophical answer depending on the current state and emotion."""
        prefix = self._emotion_prefix()
        if self.state == "Ego":
            return f"{prefix}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{prefix}Resnica je relativna, oblikovana z našimi odnosi."
        return f"{prefix}Vse resnice so eno, medsebojno povezane."

    def _emotion_prefix(self) -> str:
        """Provide a short prefix describing current emotion."""
        if self.emotion_type == Emotion.NEUTRAL:
            return ""
        return f"Po\u010dutim se {self.emotion_type.value}, zato "
