from __future__ import annotations

from typing import List
from .emotions import EmotionState


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotions: EmotionState | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or EmotionState()
        self.history: List[str] = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update a specific emotion and adjust tension."""
        self.emotions.update(name, value)
        self.tension += self.emotions.tension_influence

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotions.overall > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state and emotion."""
        mood = self._describe_mood()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} ({mood})"

    def _describe_mood(self) -> str:
        """Return a short text describing the current dominant emotion."""
        emotions = self.emotions
        dominant = max(
            [("fear", emotions.fear), ("joy", emotions.joy), ("anger", emotions.anger)],
            key=lambda item: item[1],
        )
        if dominant[1] == 0:
            return "miren"
        names = {"fear": "prestrašen", "joy": "radosten", "anger": "jezen"}
        return names.get(dominant[0], "miren")
