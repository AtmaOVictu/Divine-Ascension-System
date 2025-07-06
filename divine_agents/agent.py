from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of state transitions and dialogue."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotional_state: str = "neutral"
    loyalty: float = 0.0
    experiences: List[str] = field(default_factory=list)
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update emotion type and intensity, adjusting tension."""
        self.emotional_state = emotion
        self.emotion_level = value
        self.adjust_tension_based_on_emotions()

    def adjust_tension_based_on_emotions(self) -> None:
        """Modify tension according to current emotional state."""
        if self.emotional_state == "angry":
            self.tension += 0.3
        elif self.emotional_state == "happy":
            self.tension -= 0.2
        else:
            self.tension += 0.1

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition between states if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical response influenced by state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotional_state == "angry":
            base += " Počutim se jezen."
        elif self.emotional_state == "fearful":
            base += " Občutim strah."
        elif self.emotional_state == "happy":
            base += " Vesel sem."
        return base
