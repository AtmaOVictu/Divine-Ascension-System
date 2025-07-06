"""Ontological agents capable of philosophical state transitions."""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Agent:
    """Represents an ontological agent with emotional context."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotions: Dict[str, float] = field(default_factory=dict)
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Set emotion intensity and update tension."""
        self.emotions[emotion] = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def max_emotion(self) -> float:
        """Return the current maximum emotion intensity."""
        return max(self.emotions.values(), default=0.0)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.max_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.max_emotion() > 0.5:
            return f"{base} Moja čustva so silovita."
        return base
