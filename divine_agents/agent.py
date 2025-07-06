from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent with emotional dynamics and state transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotional_state: str = "neutral"
    emotion_intensity: float = 0.0
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, emotional_state: str, intensity: float) -> None:
        """Update emotional state and adjust tension accordingly."""
        self.emotional_state = emotional_state
        self.emotion_intensity = intensity
        if emotional_state in {"fear", "anger"}:
            self.tension += 0.3 * intensity
        elif emotional_state == "joy":
            self.tension -= 0.2 * intensity
        else:
            self.tension += 0.1 * intensity
        self.tension = max(0.0, min(1.0, self.tension))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Transition to the next ontological state if thresholds are reached."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical response based on current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
