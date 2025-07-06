class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name : str
        Name of the agent.
    state : str
        Current ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension : float
        Current tension level.
    emotion : float
        Intensity of the current emotion.
    emotion_type : str
        Qualitative description of the emotion (e.g. ``"joy"``, ``"fear"``).
    history : list[str]
        History of states the agent transitioned through.
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

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value : float
            Numerical intensity of the emotion.
        emotion_type : str, optional
            Qualitative description of the emotion.
        """
        self.emotion = value
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
        """Return a philosophical answer adjusted by emotion and state."""
        prefix = ""
        if self.emotion_type == "fear":
            prefix = "S strahom "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem "
        elif self.emotion_type == "anger":
            prefix = "Z jezo "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix}{base}"
