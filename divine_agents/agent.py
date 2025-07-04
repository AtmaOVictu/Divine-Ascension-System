class Agent:
    """Ontological agent capable of transitioning philosophical states.

    Parameters
    ----------
    name: str
        Name of the agent.
    state: str, optional
        Initial ontological state (``"Ego"`` | ``"Jaz"`` | ``"Enotnost"``).
    tension: float, optional
        Current tension level. Values above the threshold may trigger
        a state change.
    emotion: float, optional
        Intensity of the current emotion. Also contributes to tension.
    emotion_type: str, optional
        Descriptive label of the current emotion (e.g. ``"fear"`` or
        ``"joy"``). Used only for dialogue generation.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally set emotion type.

        Parameters
        ----------
        value: float
            New emotion intensity.
        emotion_type: str, optional
            Descriptive name of the emotion influencing the agent.
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        # heightened emotions increase tension
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
        """Return a philosophical answer influenced by current state and emotion."""
        prefix = ""
        if self.emotion > 0.5 and self.emotion_type:
            prefix = f"({self.emotion_type}) "

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."

        return prefix + core
