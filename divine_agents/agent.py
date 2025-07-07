"""Ontological agents capable of state transitions based on emotion and tension."""

from __future__ import annotations

from dataclasses import dataclass, field


def _clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    """Clamp a numeric value to a fixed range."""
    return max(minimum, min(maximum, value))


@dataclass
class Agent:
    """Agent that transitions between philosophical states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.tension = _clamp(self.tension)
        self.emotion = _clamp(self.emotion)
        if not self.history:
            self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Update emotion and increase tension proportionally."""
        self.emotion = _clamp(value)
        self.tension = _clamp(self.tension + value * 0.5)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = _clamp(value)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
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
