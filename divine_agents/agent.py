class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Unique identifier for the agent.
    state: str
        Current ontological state (Ego, Jaz or Enotnost).
    tension: float
        Intensity of the agent's tension.
    emotion: float
        Intensity of the agent's current emotion.
    emotion_type: str
        Descriptive label of the current emotion (e.g. 'fear', 'joy').
    history: list
        Record of states the agent has transitioned through.
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

    def update_emotion(self, value: float, kind: str | None = None) -> None:
        """Update emotion intensity and optionally set the emotion type.

        Parameters
        ----------
        value: float
            Intensity of the emotion (0 to 1).
        kind: str | None
            Name of the emotion (e.g. ``"fear"``). If ``None`` the
            previous type is preserved.
        """
        self.emotion = value
        if kind is not None:
            self.emotion_type = kind
        # The emotional intensity directly contributes to tension
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        The agent moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to
        ``Enotnost`` when either its tension exceeds ``0.7`` or its
        emotion exceeds ``0.5``. The state ``Enotnost`` is terminal in
        this simple model.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type and self.emotion > 0:
            return f"{base} Čutim {self.emotion_type}."
        return base
