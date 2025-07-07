class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Identifier of the agent.
    state: str
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension: float
        Accumulated tension influencing state transitions.
    emotion: float
        Intensity of the current emotion in range ``0-1``.
    emotion_type: str
        Qualitative description of the emotion (e.g. ``fear`` or ``joy``).
    history: list[str]
        List of states the agent has been through.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and adjust tension.

        Parameters
        ----------
        value:
            New intensity of the emotion in range ``0-1``.
        name:
            Optional textual description of the emotion.
        """
        self.emotion = value
        if name is not None:
            self.emotion_type = name
        # higher emotions raise tension and may trigger transitions
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type != "neutral":
            base += f" Čutim {self.emotion_type}."
        return base
