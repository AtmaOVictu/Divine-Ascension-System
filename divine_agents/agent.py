class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent holds an ontological ``state`` (``Ego`` -> ``Jaz`` -> ``Enotnost``)
    and may transition based on its current ``tension`` or ``emotion`` level.
    Each agent also keeps track of its dominant emotional type to influence
    responses in dialogues.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            New emotion intensity. This value also increases the agent's
            ``tension`` level.
        emotion_type: str | None, optional
            Descriptive label for the emotion (e.g. ``fear`` or ``joy``).
        """
        self.emotion = value
        self.tension += value
        if emotion_type:
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
        """Return a philosophical answer depending on the current state.

        The emotional type influences the tone of the answer.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (čustvo: {self.emotion_type})"
