"""Core agent module used for simulating ontological discussions."""

from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents an emotion with a name and intensity."""

    name: str
    intensity: float


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion("neutral", 0.0)
        self.history = [state]

    def __repr__(self) -> str:  # pragma: no cover - simple helper
        return f"Agent(name={self.name}, state={self.state}, tension={self.tension}, emotion={self.emotion})"

    def update_emotion(self, intensity: float, name: str | None = None) -> None:
        """Update emotion and adjust tension accordingly."""
        if name is not None:
            self.emotion.name = name
        self.emotion.intensity = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion.intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        prefix = f"[{self.emotion.name}:{self.emotion.intensity:.1f}]"
        if self.state == "Ego":
            return f"{prefix} Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{prefix} Resnica je relativna, oblikovana z našimi odnosi."
        return f"{prefix} Vse resnice so eno, medsebojno povezane."
