from dataclasses import dataclass, field
from enum import Enum


class State(Enum):
    """Possible ontological states for an agent."""
    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Emotions:
    """Track emotional intensities."""
    fear: float = 0.0
    joy: float = 0.0
    anger: float = 0.0

    def intensity(self) -> float:
        """Return the highest emotional intensity."""
        return max(self.fear, self.joy, self.anger)


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotions: Emotions = field(default_factory=Emotions)

    def feel(self, **kwargs) -> None:
        """Update emotions and adjust tension accordingly."""
        for emotion, value in kwargs.items():
            if hasattr(self.emotions, emotion):
                setattr(self.emotions, emotion, value)
        self.tension = self.emotions.intensity()

    def update_state(self) -> None:
        """Transition to the next state if thresholds are exceeded."""
        triggered = self.tension > 0.7 or self.emotions.intensity() > 0.5
        if self.state == State.EGO and triggered:
            self.state = State.JAZ
        elif self.state == State.JAZ and triggered:
            self.state = State.ENOTNOST

    def respond(self) -> str:
        """Return a philosophical response based on the current state."""
        if self.state == State.EGO:
            return f"{self.name}: Truth is absolute and independent of others."
        if self.state == State.JAZ:
            return f"{self.name}: Truth is relative, shaped by our relationships."
        return f"{self.name}: All truths are one and interconnected."
