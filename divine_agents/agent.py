from dataclasses import dataclass, field
from typing import Dict, List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: Dict[str, float] | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: Dict[str, float] = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history: List[str] = [state]

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotions[emotion] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        max_emotion = max(self.emotions.values()) if self.emotions else 0.0
        if self.tension > 0.7 or max_emotion > 0.5:
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
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
