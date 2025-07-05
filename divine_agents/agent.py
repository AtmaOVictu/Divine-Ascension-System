"""Ontological agent capable of transitioning between states.

This module defines the Agent class used to model transitions between
philosophical states (Ego, Jaz, Enotnost) influenced by emotion and
tension levels.
"""

from typing import List


class Agent:
    """Represents an ontological agent."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion = emotion
        self.history: List[str] = [state]

    def update_emotion(self, value: float, kind: str) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_level = value
        self.emotion = kind
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _base_response(self) -> str:
        """Return the philosophical statement for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a response influenced by the agent's emotion."""
        base = self._base_response()
        if self.emotion == "fear":
            prefix = "S strahom povem, da "
        elif self.emotion == "joy":
            prefix = "Z veseljem verjamem, da "
        elif self.emotion == "anger":
            prefix = "Z jezo zagovarjam, da "
        else:
            prefix = ""
        return prefix + base
