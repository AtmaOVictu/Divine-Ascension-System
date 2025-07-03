from dataclasses import dataclass, field


@dataclass
class Agent:
    """Ontological agent capable of emotional transitions between states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_name: str = "neutral"
    history: list[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float, name: str = "") -> None:
        """Update emotional intensity and adjust tension.

        Parameters
        ----------
        value: float
            New emotional intensity.
        name: str, optional
            Descriptive label of the emotion (e.g. 'jeza', 'strah').
        """
        self.emotion = value
        if name:
            self.emotion_name = name
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension thresholds are exceeded."""
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

    def speak(self, question: str) -> str:
        """Compose a line of dialogue including emotional state."""
        answer = self.respond(question)
        return f"{self.name} ({self.state}, {self.emotion_name}:{self.emotion:.1f}): {answer}"
