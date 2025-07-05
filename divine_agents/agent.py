class Agent:
    """Ontological agent capable of emotional transitions between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion  # intensity
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity, optionally setting the emotion type."""
        self.emotion = value
        if name is not None:
            self.emotion_type = name
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
        emotion_txt = f" (čutim {self.emotion_type})" if self.emotion_type else ""
        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih.{emotion_txt}"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z našimi odnosi.{emotion_txt}"
        return f"Vse resnice so eno, medsebojno povezane.{emotion_txt}"
