class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    EMOTION_INTENSITY = {
        "fear": 0.6,
        "joy": 0.8,
        "anger": 0.7,
        "sorrow": 0.4,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value : str | float
            Named emotion (``"fear"``) or direct intensity.
        """
        if isinstance(value, str):
            intensity = self.EMOTION_INTENSITY.get(value, 0.0)
            self.emotion_label = value
        else:
            intensity = float(value)
            self.emotion_label = "custom"
        self.emotion = intensity
        self.tension += intensity

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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label and self.emotion_label != "neutral":
            base += f" Čutim {self.emotion_label}."
        return base
