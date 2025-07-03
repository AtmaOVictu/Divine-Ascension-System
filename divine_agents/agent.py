class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: How much each emotion influences tension. Positive values increase
    #: tension and negative values calm the agent.
    EMOTION_EFFECTS = {
        "fear": 0.3,
        "joy": -0.1,
        "anger": 0.4,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_name: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update emotion intensity and adjust tension according to emotion."""
        self.emotion_name = name
        self.emotion = value
        self.tension += value + self.EMOTION_EFFECTS.get(name, 0.0)

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
        emotion_part = f" ({self.emotion_name})" if self.emotion_name else ""
        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih.{emotion_part}"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z našimi odnosi.{emotion_part}"
        return f"Vse resnice so eno, medsebojno povezane.{emotion_part}"
