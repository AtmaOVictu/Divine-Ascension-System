from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


class Agent:
    """Ontological agent capable of transitioning between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotions: Dict[str, float] | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        # store several emotions and their intensities
        self.emotions: Dict[str, float] = {
            "fear": 0.0,
            "joy": 0.0,
            "anger": 0.0,
            "sorrow": 0.0,
        }
        if emotions:
            self.emotions.update(emotions)
        self.history: List[str] = [state]

    # ------------------------------------------------------------------
    # Emotion and tension management
    # ------------------------------------------------------------------
    def update_emotion(self, name: str, value: float) -> None:
        """Set the intensity of an emotion and adjust tension."""
        self.emotions[name] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def dominant_emotion(self) -> str | None:
        """Return the emotion with the highest intensity."""
        if not self.emotions:
            return None
        return max(self.emotions, key=self.emotions.get)

    # ------------------------------------------------------------------
    # Ontological state management
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or max(self.emotions.values(), default=0.0) > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current state and emotion."""
        emotion = self.dominant_emotion()
        prefix = f"({emotion}) " if emotion and self.emotions[emotion] > 0.5 else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
