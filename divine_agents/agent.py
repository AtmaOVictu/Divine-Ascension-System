from dataclasses import dataclass, field


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.tension = self._clamp(self.tension)
        self.emotion = self._clamp(self.emotion)
        self.history.append(self.state)

    @staticmethod
    def _clamp(value: float) -> float:
        """Ensure a value is within the [0, 1] range."""
        return max(0.0, min(1.0, value))

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = self._clamp(value)
        self.tension = self._clamp(self.tension + self.emotion)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = self._clamp(value)

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
