from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Agent:
    """Ontological agent capable of emotional transitions between states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: Optional[str] = None
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.emotion = value
        self.emotion_type = emotion_type
        if emotion_type in {"fear", "anger"}:
            self.tension = min(1.0, self.tension + value)
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - value)
        else:
            self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer shaped by state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type:
            return f"[{self.emotion_type}] {base}"
        return base
