"""Ontological agent capable of transitioning states based on emotion and tension."""

from dataclasses import dataclass, field
from typing import List


STATE_PRINCIPLES = {
    "Ego": "Resnica je absolutna in neodvisna od drugih.",
    "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
    "Enotnost": "Vse resnice so eno, medsebojno povezane.",
}

EMOTION_THRESHOLD = 0.5
TENSION_THRESHOLD = 0.7


@dataclass
class Agent:
    """Represents an ontological agent."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(value, 1.0))
        self.tension = min(1.0, self.tension + self.emotion)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(value, 1.0))

    def intensity(self) -> float:
        """Return current intensity based on tension and emotion."""
        return self.tension * self.emotion

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceeds thresholds."""
        if self.tension > TENSION_THRESHOLD or self.emotion > EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def principle(self) -> str:
        """Return the philosophical principle of the current state."""
        return STATE_PRINCIPLES[self.state]

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = self.principle()
        
        if self.emotion > 0.7:
            base += " Moja čustva so zelo močna."
        elif self.emotion > 0.3:
            base += " Čutim rahlo napetost."

        return base
