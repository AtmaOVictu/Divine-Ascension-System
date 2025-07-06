from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of state transitions and dialogue."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotional_state: str = "neutral"
    loyalty: float = 0.5
    experiences: List[str] = field(default_factory=list)
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, intensity: float, mood: str) -> None:
        """Set emotion intensity and mood, adjusting tension."""
        self.emotion = intensity
        self.emotional_state = mood
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def add_experience(self, experience: str) -> None:
        """Record a new experience."""
        self.experiences.append(experience)

    def transition(self) -> str:
        """Perform basic transition based on emotion or tension thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def multi_layer_transition(self) -> str:
        """Transition considering experiences and loyalty in addition to thresholds."""
        last_experience = self.experiences[-1] if self.experiences else "neutral"
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                if self.loyalty > 0.8 or "selfish" in last_experience:
                    self.state = "Jaz"
            elif self.state == "Jaz":
                if self.loyalty > 0.8 or "unifying" in last_experience:
                    self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on current state and mood."""
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"[{self.emotional_state}] {base}"
