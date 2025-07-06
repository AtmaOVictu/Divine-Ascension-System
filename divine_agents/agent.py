class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Identifier for the agent.
    state: str, optional
        Initial ontological state. Defaults to ``"Ego"``.
    tension: float, optional
        Starting tension level in the range ``0-1``.
    emotion: float, optional
        Starting emotion intensity in the range ``0-1``.
    emotion_type: str, optional
        Descriptive label for the current dominant emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension and emotion type.

        Parameters
        ----------
        value:
            New emotion intensity in the range ``0-1``.
        emotion_type:
            Optional descriptive label such as ``"fear"`` or ``"joy"``.
        """
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
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
        """Return a philosophical answer shaped by state and emotion."""
        prefix = {
            "fear": "S strahom ",
            "joy": "Veselo ",
            "anger": "Jezeno ",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{base}"
