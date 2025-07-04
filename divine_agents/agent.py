class Agent:
    """Ontological agent capable of transitioning states.

    Parameters
    ----------
    name : str
        Agent identifier.
    state : str, optional
        Initial ontological state, by default ``"Ego"``.
    tension : float, optional
        Initial tension level, by default ``0.0``.
    emotion : float, optional
        Intensity of the current emotion, by default ``0.0``.
    emotion_type : str, optional
        Name of the current emotion, e.g. ``"fear"`` or ``"joy"``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        emotion_type : str
            Name of the emotion being experienced.
        value : float
            Intensity of the emotion which contributes to tension.
        """
        self.emotion_type = emotion_type
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

    def describe_state(self) -> str:
        """Return a human readable description of current state and emotion."""
        if self.emotion_type:
            return f"{self.state} (tension={self.tension:.2f}, emotion={self.emotion_type}:{self.emotion:.2f})"
        return f"{self.state} (tension={self.tension:.2f})"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type:
            return f"{base} Občutim {self.emotion_type}."
        return base
