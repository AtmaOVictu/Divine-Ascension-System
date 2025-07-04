from __future__ import annotations

from .utils import log_history


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "neutral", log_path: str = "history_log.txt"):
        """Create a new agent.

        Parameters
        ----------
        name:
            Identifier for the agent.
        state:
            Initial ontological state.
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity.
        emotion_type:
            Description of the current dominant emotion.
        log_path:
            File path where transitions will be logged.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.log_path = log_path
        self.emotion_type = emotion_type

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally set emotion type."""
        self.emotion = value
        if emotion_type is not None:
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
            log_history(f"{self.name} transitioned to {self.state}", path=self.log_path)
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer reflecting the current state and emotion."""
        mood = f"(obcutek: {self.emotion_type})" if self.emotion_type != "neutral" else ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z nasimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} {mood}".strip()
