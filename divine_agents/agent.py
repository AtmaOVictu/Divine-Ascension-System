class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Name of the agent.
    state: str
        Current ontological state.
    tension: float
        Accumulated tension of the agent.
    emotion: float
        Current emotion intensity.
    emotion_label: str
        Name of the current emotion (fear, joy, anger, etc.).
    history: list[str]
        History of states during transitions.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotion_label: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            New emotion intensity.
        label: str, optional
            Name of the emotion influencing the agent.
        """
        self.emotion = value
        if label is not None:
            self.emotion_label = label
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
        """Return a philosophical answer depending on the current state."""
        prefix = f"[{self.emotion_label}:{self.emotion:.1f}]"
        if self.state == "Ego":
            return f"{prefix} Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{prefix} Resnica je relativna, oblikovana z našimi odnosi."
        return f"{prefix} Vse resnice so eno, medsebojno povezane."
