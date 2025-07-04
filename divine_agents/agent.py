class Agent:
    """Ontological agent that transitions between Ego, Jaz and Enotnost.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Starting ontological state. Defaults to ``"Ego"``.
    tension:
        Current tension level in the agent.
    emotion:
        Intensity of the current emotion.
    emotion_type:
        Optional string describing the current emotion (e.g. ``"fear"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotional state.

        Parameters
        ----------
        value:
            New emotion intensity. This value also increases ``tension``.
        emotion_type:
            Optional name of the emotion (e.g. ``"joy"`` or ``"fear"``).
        """
        self.emotion = value
        self.tension += value
        if emotion_type is not None:
            self.emotion_type = emotion_type

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
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type:
            return f"{base} \u2013 Ob\u010dutam {self.emotion_type}."
        return base

    def __repr__(self) -> str:
        return (
            f"Agent(name={self.name!r}, state={self.state!r}, tension={self.tension}, "
            f"emotion={self.emotion}, emotion_type={self.emotion_type!r})"
        )
