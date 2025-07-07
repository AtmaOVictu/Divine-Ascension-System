from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent that transitions between philosophical states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set tension level directly."""
        self.tension = value

    def transition(self) -> str:
        """Transition states if thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical response based on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            return f"{base} Čutim močna čustva."
        if self.emotion > 0.3:
            return f"{base} Moja čustva me usmerjajo."
        return base
