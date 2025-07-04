class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        """Initialize the agent with its ontological state and emotions."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, emotion_type: str, value: float) -> None:
        """Set the current emotional type and intensity."""
        self.emotion_type = emotion_type
        self.update_emotion(value)

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded."""
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
                f"V svojem {self.emotion_type} verjamem, da je resnica "
                "absolutna in neodvisna od drugih."
            )
        if self.state == "Jaz":
            return (
                f"V čustvu {self.emotion_type} menim, da je resnica relativna, "
                "oblikovana z našimi odnosi."
            )
        return (
            f"Z občutkom {self.emotion_type} vidim, da so vse resnice eno, "
            "medsebojno povezane."
        )
