"""Core logic for ontological agents and their state transitions."""

from __future__ import annotations

from typing import Dict


EMO_TRANSLATIONS = {
    "fear": "strah",
    "joy": "veselje",
    "anger": "jeza",
}


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: Dict[str, float] | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: Dict[str, float] = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def emotion_level(self) -> float:
        """Return the highest emotion intensity."""
        return max(self.emotions.values(), default=0.0)

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update an emotion and adjust tension accordingly."""
        self.emotions[emotion] = value
        if value > self.tension:
            self.tension = value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        mood = max(self.emotions, key=self.emotions.get)
        prefix = ""
        if self.emotions[mood] > 0.5:
            prefix = f"Občutim {EMO_TRANSLATIONS.get(mood, mood)}. "

        if self.state == "Ego":
            message = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            message = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            message = "Vse resnice so eno, medsebojno povezane."

        return prefix + message
