class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Identifier for the agent.
    state: str
        Initial ontological state (``"Ego"``|``"Jaz"``|``"Enotnost"``).
    tension: float
        Current level of tension driving state changes.
    emotion: float
        Intensity of the current emotion.
    emotion_type: str
        Descriptor of the emotion (e.g. ``"fear"``, ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def set_emotion(self, emotion_type: str, value: float) -> None:
        """Set the current emotion type and intensity.

        Parameters
        ----------
        emotion_type: str
            Name of the emotion (e.g. ``"fear"``, ``"joy"``).
        value: float
            Intensity of the emotion in ``[0, 1]``.
        """
        self.emotion_type = emotion_type
        self.emotion = value
        self.tension += value

    def update_emotion(self, value: float) -> None:
        """Backward compatible wrapper for setting unnamed emotion."""
        self.set_emotion(self.emotion_type, value)

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
        prefix = f"Občutim {self.emotion_type}, zato menim: "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
