class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_name: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if name is not None:
            self.emotion_name = name
        # Emotion intensity contributes to overall tension
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
        if self.state == "Ego":
            return (
                f"Čutim {self.emotion_name}, zato verjamem, da je resnica absolutna "
                "in neodvisna od drugih."
            )
        if self.state == "Jaz":
            return (
                f"Ker sem {self.emotion_name}, menim, da je resnica relativna in "
                "oblikovana z našimi odnosi."
            )
        return (
            f"Z občutkom {self.emotion_name} spoznavam, da so vse resnice eno, "
            "medsebojno povezane."
        )
