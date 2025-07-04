class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Display name of the agent.
    state: str
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension: float
        Numerical measure of internal tension.
    emotion: float
        Current emotional intensity in the ``[0, 1]`` range.
    emotion_type: str
        Label describing the dominant emotion (e.g. ``fear`` or ``joy``).
    history: list[str]
        List of previously visited states.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_type: str | None = None) -> None:
        """Initialize the agent with optional emotional context."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally set the emotion label."""
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
        """Return a philosophical answer influenced by the current emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5 and self.emotion_type != "neutral":
            return f"{base} (\u010ditim {self.emotion_type})."
        return base
