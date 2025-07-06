from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotional_state: str = "neutral"
    loyalty: float = 0.0
    experiences: List[str] = field(default_factory=list)
    history: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def set_emotional_state(self, emotion_label: str, intensity: float) -> None:
        """Set the current emotional state and adjust tension accordingly."""
        self.emotional_state = emotion_label
        self.emotion = intensity
        self.adjust_tension_based_on_emotions()

    def adjust_tension_based_on_emotions(self) -> None:
        """Modify tension depending on the agent's emotional state."""
        if self.emotional_state in {"anger", "fear"}:
            self.tension += 0.3
        elif self.emotional_state == "joy":
            self.tension = max(0.0, self.tension - 0.2)
        else:
            self.tension += 0.1

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def add_experience(self, experience: str) -> None:
        self.experiences.append(experience)

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
        """Return a philosophical response based on current ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
