"""Ontological agent model with emotion-driven state transitions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Emotions:
    """Simple container for emotional intensities."""

    fear: float = 0.0
    joy: float = 0.0
    anger: float = 0.0

    def intensity(self) -> float:
        """Return the highest emotional value as overall intensity."""
        return max(self.fear, self.joy, self.anger)


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension = 0.0
        self.emotions = Emotions()
        self.history: List[Tuple[str, float, float]] = [(state, 0.0, 0.0)]
        self.cluster: int | None = None

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def feel(self, **kwargs: float) -> None:
        """Update specific emotions and recalculate tension."""

        for key, value in kwargs.items():
            if hasattr(self.emotions, key):
                setattr(self.emotions, key, value)
        self.tension = max(self.tension, self.emotions.intensity())
        self.history.append((self.state, self.tension, self.emotions.intensity()))

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""

        self.tension = value
        self.history.append((self.state, self.tension, self.emotions.intensity()))

    # ------------------------------------------------------------------
    # State transitions
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""

        triggered = self.tension > 0.7 or self.emotions.intensity() > 0.5
        if triggered:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append((self.state, self.tension, self.emotions.intensity()))
        return self.state

    # ------------------------------------------------------------------
    # Dialogue helpers
    # ------------------------------------------------------------------
    def _emotion_descriptor(self) -> str:
        """Return a word describing dominant emotion."""

        emo = self.emotions
        if emo.fear > 0.5:
            return "fearfully"
        if emo.joy > 0.5:
            return "joyfully"
        if emo.anger > 0.5:
            return "angrily"
        return "calmly"

    def respond(self, _question: str) -> str:
        """Return a philosophical answer reflecting state and emotion."""

        mood = self._emotion_descriptor()

        if self.state == "Ego":
            answer = "Truth is absolute and independent of others."
        elif self.state == "Jaz":
            answer = "Truth is relative, shaped by our relationships."
        else:
            answer = "All truths are one and interconnected."
        return f"{self.name} ({mood}) says: {answer}"

    # ------------------------------------------------------------------
    # Learning / clustering
    # ------------------------------------------------------------------
    def learn_from_history(self) -> int:
        """Assign a simple cluster based on average tension."""

        if not self.history:
            self.cluster = 0
            return self.cluster

        max_tension = max(h[1] for h in self.history)
        if max_tension < 0.3:
            self.cluster = 0
        elif max_tension < 0.7:
            self.cluster = 1
        else:
            self.cluster = 2
        return self.cluster

