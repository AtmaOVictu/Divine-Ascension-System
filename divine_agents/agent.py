"""Ontological agent capable of philosophical state transitions."""
from __future__ import annotations


class Agent:
    """Represents an ontological agent with emotion and tension levels."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: str = "neutral", emotion_intensity: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = self._clamp(tension)
        self.emotion = emotion
        self.emotion_intensity = self._clamp(emotion_intensity)
        self.history = [state]

    @staticmethod
    def _clamp(value: float) -> float:
        """Clamp a value between 0 and 100."""
        return max(0.0, min(100.0, value))

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Update the agent's emotion and adjust tension."""
        self.emotion = emotion
        self.emotion_intensity = self._clamp(intensity)
        self.tension = self._clamp(self.tension + self.emotion_intensity)

    def update_tension(self, value: float) -> None:
        """Directly set tension level in percentage."""
        self.tension = self._clamp(value)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 70 or self.emotion_intensity > 50:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_suffix = {
            "fear": " Občutim strah.",
            "joy": " Občutim veselje.",
            "anger": " Občutim jezo.",
            "sorrow": " Občutim žalost.",
        }.get(self.emotion, "")
        return f"{base}{emotion_suffix}"
