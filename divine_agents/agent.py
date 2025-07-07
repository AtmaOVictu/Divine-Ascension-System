"""Ontological agents capable of transitioning states and learning."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Agent:
    """Represents an ontological agent with emotion based transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[Tuple[str, float, float]] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append((self.state, self.tension, self.emotion))

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.history.append(("emotion_update", self.tension, self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.history.append(("tension_update", self.tension, self.emotion))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(("transition", self.tension, self.emotion))
        return self.state

    def reward(self, result: bool) -> None:
        """Reinforce the agent based on success or failure."""
        delta = 0.1 if result else -0.1
        self.emotion += delta
        self.history.append(("reward", self.tension, self.emotion))

    def respond(self, _: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
