class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_name: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = float(tension)
        self.emotion = float(emotion)
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotional intensity.
        name:
            Optional textual description of the emotion (e.g. ``"fear"``).
        """
        self.emotion = float(value)
        self.tension += value
        if name is not None:
            self.emotion_name = name

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
                f"Po mojih občutkih ({self.emotion_name}) je resnica absolutna "
                "in neodvisna od drugih."
            )
        if self.state == "Jaz":
            return (
                f"Kot dojemam skozi {self.emotion_name}, je resnica relativna in "
                "oblikovana z našimi odnosi."
            )
        return (
            f"V skladu z mojim občutkom {self.emotion_name} vidim, da so vse "
            "resnice eno, medsebojno povezane."
        )
