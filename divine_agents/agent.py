"""Agent module implementing ontological transitions and responses."""
from __future__ import annotations


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name or "neutral"
        self.history: list[str] = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and optionally label the emotion."""
        self.emotion = value
        if name:
            self.emotion_name = name
        # Tension rises with emotional intensity
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next ontological state if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current state."""
        if self.state == "Ego":
            return (
                "Resnica je absolutna in neodvisna od drugih. "
                f"Čutim {self.emotion_name}."
            )
        if self.state == "Jaz":
            return (
                "Resnica je relativna, oblikovana z našimi odnosi. "
                f"Čutim {self.emotion_name}."
            )
        return (
            "Vse resnice so eno, medsebojno povezane. "
            f"Čutim {self.emotion_name}."
        )

