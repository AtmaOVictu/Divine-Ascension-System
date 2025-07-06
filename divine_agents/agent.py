"""Core logic for ontological agents and their state transitions."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_name: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set emotion type and intensity, increasing tension accordingly."""
        self.emotion_name = name
        self.emotion = intensity
        self.tension += intensity

    # Backwards compatible helper
    def update_emotion(self, value: float) -> None:  # pragma: no cover - legacy
        self.set_emotion("neutral", value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def philosophical_principle(self) -> str:
        """Return the philosophical statement for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Answer a question, reflecting state and current emotion."""
        principle = self.philosophical_principle()
        return f"{principle} (Čustvo: {self.emotion_name})"
