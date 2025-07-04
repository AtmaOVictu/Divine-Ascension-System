"""Core agent implementation used for philosophical simulations."""

from __future__ import annotations

import math
from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = (
        "Ego",
        "Jaz",
        "Enotnost",
        "Absolutna resnica",
        "Relativna resnica",
        "Povezana resnica",
    )

    #: Mapping of emotions to their impact on tension
    EMOTION_IMPACT = {
        "fear": 0.4,
        "anger": 0.6,
        "joy": 0.2,
        "sorrow": 0.5,
        "love": 0.3,
        "hatred": 0.7,
    }

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_label: str = "neutral",
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history: List[str] = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def apply_emotion(self, emotion: str) -> None:
        """Set an emotion label and update tension accordingly."""
        self.emotion_label = emotion
        self.update_emotion(self.EMOTION_IMPACT.get(emotion, 0.0))

    def resolve_conflict(self) -> None:
        """Handle conflicting emotional states like love and hatred."""
        if "love" in self.emotion_label and "hatred" in self.emotion_label:
            self.emotion_label = "neutral"
            self.tension = 0.5

    def regulate_tension(self) -> float:
        """Regulate tension using a logarithmic scale to avoid sudden jumps."""
        self.tension = math.log(self.tension + 1)
        return self.tension

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
            elif self.state == "Enotnost":
                self.state = "Absolutna resnica"
            elif self.state == "Absolutna resnica":
                self.state = "Relativna resnica"
            elif self.state == "Relativna resnica":
                self.state = "Povezana resnica"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        elif self.state == "Enotnost":
            base = "Vse resnice so eno, medsebojno povezane."
        elif self.state == "Absolutna resnica":
            base = "Resnica je vseobsegajoča in brezpogojna."
        elif self.state == "Relativna resnica":
            base = "Resnica je odvisna od perspektive in okolja."
        else:  # Povezana resnica
            base = "Resnica se oblikuje v povezavi med vsemi stvarmi."

        if self.emotion_label != "neutral":
            return f"{base} (Čustvo: {self.emotion_label})"
        return base
