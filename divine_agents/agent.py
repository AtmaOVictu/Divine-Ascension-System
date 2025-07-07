"""Ontological agents and interactions."""

from __future__ import annotations


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = self._clamp(tension)
        self.emotion = self._clamp(emotion)
        self.history = [state]

    @staticmethod
    def _clamp(value: float) -> float:
        """Clamp numeric values between 0 and 1."""
        return max(0.0, min(1.0, value))

    def update_emotion(self, value: float) -> None:
        """Update emotional intensity and reflect it in tension."""
        self.emotion = self._clamp(value)
        # emotional spikes increase tension but remain normalised
        self.tension = self._clamp(self.tension + self.emotion)

    def update_tension(self, value: float) -> None:
        """Directly set tension level, normalised between 0 and 1."""
        self.tension = self._clamp(value)

    def transition(self) -> str:
        """Perform a state transition if tension or emotion exceed thresholds."""
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
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
            return (
                "Resnica je relativna, oblikovana z našimi odnosi. "
                f"Čustvo: {self.emotion:.0%}."
            )
        return (
            "Vse resnice so eno, medsebojno povezane. "
            f"Napetost: {self.tension:.0%}."
        )
