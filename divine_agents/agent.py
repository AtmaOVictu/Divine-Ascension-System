class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Agent identifier.
    state: str, optional
        Starting ontological state (default ``"Ego"``).
    tension: float, optional
        Initial tension level.
    emotion: float, optional
        Initial emotion intensity. ``0`` means neutral.
    emotion_label: str, optional
        Human readable label of the current emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_label: str = "neutral",
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, label: str, value: float) -> None:
        """Update emotion label and intensity while adjusting tension.

        Parameters
        ----------
        label: str
            Descriptive name of the emotion (e.g. ``"fear"``).
        value: float
            Intensity of the emotion in range ``0``-``1``.
        """
        self.emotion_label = label
        self.emotion = value
        # Emotional intensity contributes to tension build up
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
        """Return a philosophical answer depending on the current state.

        The answer also reflects the agent's current emotion.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (Čustvo: {self.emotion_label})"
