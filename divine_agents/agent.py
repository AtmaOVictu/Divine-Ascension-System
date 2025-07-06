class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_label: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, label: str, value: float) -> None:
        """Update emotion intensity and label and adjust tension."""
        self.emotion_label = label
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
        """Return a philosophical answer depending on the current state."""
        emotion_note = "" if not self.emotion_label else f"Obcutim {self.emotion_label}. "
        if self.state == "Ego":
            return f"{emotion_note}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{emotion_note}Resnica je relativna, oblikovana z nasimi odnosi."
        return f"{emotion_note}Vse resnice so eno, medsebojno povezane."
