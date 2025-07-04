"""Core agent logic for ontological state transitions and responses."""

from __future__ import annotations


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Set emotion intensity and type while adjusting tension."""
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
            if self.emotion_type == "anger":
                return base + " Ne dovolim, da mi kdo oporeka!"
            if self.emotion_type == "fear":
                return base + " Vsak dvom me plaši."  # fear
            return base
        if self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
            if self.emotion_type == "joy":
                return base + " Veseli me, da to deliva."  # joy
            return base
        return "Vse resnice so eno, medsebojno povezane."
