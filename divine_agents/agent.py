class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Initial tension level.
    emotion:
        Initial intensity of the current emotion.
    emotion_name:
        Name describing the current emotional state (e.g. ``"fear"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_name: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = float(tension)
        self.emotion = float(emotion)
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the new emotion in the range ``0.0`` - ``1.0``.
        name:
            Human readable name of the emotion (e.g. ``"fear"``).
        """

        self.emotion = float(value)
        self.emotion_name = name
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

        The agent's current emotional state influences the tone of the
        response.
        """

        prefix = ""
        if self.emotion_name == "fear":
            prefix = "S strahom povem: "
        elif self.emotion_name == "joy":
            prefix = "Z veseljem povem: "
        elif self.emotion_name == "anger":
            prefix = "Z jezo razglašam: "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
