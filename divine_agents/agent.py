class Agent:
    """Ontological agent that can transition through philosophical states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Starting ontological state. One of :data:`STATES`.
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity.
    emotion_type:
        Label describing the current emotion (``"neutral"`` by default).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
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
            New intensity in the ``[0, 1]`` range.
        emotion_type:
            Optional label describing the emotion.
        """

        self.emotion = value
        if emotion_type is not None:
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
        """Return a philosophical answer based on the current state and emotion."""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        prefix = ""
        if self.emotion > 0.5 or self.tension > 0.7:
            if self.emotion_type == "anger":
                prefix = "Z jezo povem, "
            elif self.emotion_type == "fear":
                prefix = "S strahom povem, "
            elif self.emotion_type == "joy":
                prefix = "Z veseljem povem, "

        return prefix + base
