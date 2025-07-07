class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        """Initialize a new agent.

        Parameters
        ----------
        name: str
            Name of the agent.
        state: str, optional
            Current ontological state of the agent.
        tension: float, optional
            Current tension level.
        emotion: float, optional
            Current emotion intensity in the ``[0, 1]`` range.
        emotion_type: str, optional
            Descriptive label of the current emotion (e.g. ``fear`` or ``joy``).
        """
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
        value: float
            New emotion intensity.
        emotion_type: str, optional
            Label for the emotion influencing the agent.
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
        """Return a philosophical answer influenced by current state and emotion."""

        if self.emotion_type == "fear":
            prefix = "V strahu povem, da "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem povem, da "
        elif self.emotion_type == "anger":
            prefix = "Z jezo trdim, da "
        else:
            prefix = ""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return prefix + base
