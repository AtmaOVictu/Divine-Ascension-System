"""Core primitives for ontological agents used in the dialogue system."""

from dataclasses import dataclass, field
from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion_level: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_type = emotion_type
        self.history: List[str] = [state]

    # ------------------------------------------------------------------
    # Update helpers
    # ------------------------------------------------------------------
    def update_emotion(self, emotion_type: str, level: float) -> None:
        """Set the current emotion and adjust tension."""
        self.emotion_type = emotion_type
        self.emotion_level = level
        self.tension += level

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

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type == "fear":
            return f"{base} Občutim strah ob tej razpravi."
        if self.emotion_type == "joy":
            return f"{base} Veseli me razprava."
        if self.emotion_type == "anger":
            return f"{base} Čutim jezo v tej izmenjavi."
        return base
