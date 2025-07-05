from dataclasses import dataclass, field


@dataclass
class Agent:
    """Ontological agent capable of emotional transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_label: str | None = None
    history: list[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Set emotion value, optionally updating the label, and adjust tension."""
        self.emotion = value
        if label:
            self.emotion_label = label
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotional thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on current ontological state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }
        mood = f" Občutim {self.emotion_label}." if self.emotion_label else ""
        return base.get(self.state, "") + mood
