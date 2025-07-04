"""Agent model handling state transitions and philosophical responses."""

from __future__ import annotations

import math


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

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
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def apply_emotion(self, emotion: str) -> None:
        """Set an emotion label and update tension accordingly."""
        self.emotion_label = emotion
        self.update_emotion(self.EMOTION_IMPACT.get(emotion, 0.0))

    def resolve_conflict(self) -> None:
        """Neutralise tension when opposite emotions are present."""
        if "love" in self.emotion_label and "hatred" in self.emotion_label:
            self.apply_emotion("neutral")
            self.tension = 0.5

    def regulate_tension(self) -> float:
        """Regulate tension on a logarithmic scale to avoid sharp jumps."""
        self.tension = math.log(self.tension + 1)
        return self.tension

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # Ontological transitions
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Philosophical responses
    # ------------------------------------------------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label != "neutral":
            return f"{base} (\u010custvo: {self.emotion_label})"
        return base
