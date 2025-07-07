class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Numerical representation of the agent's inner tension.
    emotion:
        Intensity of the current emotional state. Used together with
        ``emotion_type`` to determine transitions.
    emotion_type:
        Human readable description of the current emotion (e.g. ``"fear"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the new emotion.
        emotion_type:
            Optional textual description of the emotion. When provided,
            ``self.emotion_type`` will be updated.
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return (
                "Resnica je absolutna in neodvisna od drugih. "
                f"(občutek: {self.emotion_type})"
            )
        if self.state == "Jaz":
            return (
                "Resnica je relativna, oblikovana z našimi odnosi. "
                f"(občutek: {self.emotion_type})"
            )
        return (
            "Vse resnice so eno, medsebojno povezane. "
            f"(občutek: {self.emotion_type})"
        )
