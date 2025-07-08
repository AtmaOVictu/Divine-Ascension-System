"""Agent module implementing basic ontological transitions and interactions."""

from __future__ import annotations

from typing import Iterable

from .emotion import Emotion


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_state: Emotion | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_state = emotion_state or Emotion()
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.emotion_state.joy = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def interact(self, others: Iterable["Agent"], influence_factor: float = 0.2) -> None:
        """Modify emotion based on the emotional state of other agents."""
        emotions = [agent.emotion for agent in others]
        influence = sum(emotions) * influence_factor
        self.emotion += influence
        self.emotion = max(min(self.emotion, 1), -1)
        self.tension += influence

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_intensity = max(self.emotion, self.emotion_state.intensity())
        if self.tension > 0.7 or emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = ""
        if self.emotion_state.anger > 0.5:
            prefix = "Z jezo, "
        elif self.emotion_state.joy > 0.5:
            prefix = "Z veseljem, "

        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix}{answer}"
