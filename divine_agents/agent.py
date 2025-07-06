class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label or ""
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and label, adjusting tension accordingly."""
        self.emotion = value
        if label is not None:
            self.emotion_label = label
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
        """Return a philosophical answer influenced by state and emotion."""
        emotion_note = f" (občutim {self.emotion_label})" if self.emotion_label else ""

        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih.{emotion_note}"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z našimi odnosi.{emotion_note}"
        return f"Vse resnice so eno, medsebojno povezane.{emotion_note}"
