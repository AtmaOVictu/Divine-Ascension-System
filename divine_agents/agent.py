from dataclasses import dataclass, field


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")
    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __post_init__(self) -> None:
        # Initialize history with the provided starting state
        self.history = [self.state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

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
        """Return a philosophical answer influenced by the current emotion."""
        base = self.PHILOSOPHY.get(self.state, "")
        emotion_tag = self._emotion_descriptor()
        return f"{base} ({emotion_tag})"

    def _emotion_descriptor(self) -> str:
        """Return a short textual description of the current emotional level."""
        if self.emotion < 0.3:
            return "mirno"
        if self.emotion < 0.6:
            return "napeto"
        return "strastno"
