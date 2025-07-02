from dataclasses import dataclass, field


@dataclass
class Agent:
    """Represents an ontological agent with emotional and tension-based state transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list = field(default_factory=list)

    TENSION_THRESHOLD: float = 0.7
    EMOTION_THRESHOLD: float = 0.5

    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.check_transition()

    def check_transition(self) -> str:
        """Trigger state transition when thresholds are exceeded."""
        if self.state == "Ego" and (
            self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD
        ):
            self.state = "Jaz"
        elif self.state == "Jaz" and (
            self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD
        ):
            self.state = "Enotnost"
        if self.history is not None:
            self.history.append(self.state)
        return self.state

    def philosophical_response(self) -> str:
        """Return a philosophical statement based on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna in oblikovana z našimi odnosi."
        if self.state == "Enotnost":
            return "Vse resnice so eno, medsebojno povezane."
        return ""
