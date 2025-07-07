class Agent:
    """Represent an ontological agent that can transition between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or ""
        self.history: list[str] = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set the current emotion and adjust tension."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next ontological state when thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state."""
        emotion_suffix = f" Čutim {self.emotion_type}." if self.emotion_type else ""
        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih.{emotion_suffix}"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z našimi odnosi.{emotion_suffix}"
        return f"Vse resnice so eno, medsebojno povezane.{emotion_suffix}"

