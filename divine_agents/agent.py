from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotions: Dict[str, float] = field(default_factory=dict)
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, name: str, intensity: float) -> None:
        """Register an emotion and update tension."""
        self.emotions[name] = intensity
        self.update_emotion(intensity)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

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
        prefix = "Čustveno, " if self.emotion > 0.5 else ""
        if self.state == "Ego":
            return f"{prefix}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{prefix}Resnica je relativna, oblikovana z našimi odnosi."
        return f"{prefix}Vse resnice so eno, medsebojno povezane."
