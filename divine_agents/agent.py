class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Identifier for the agent.
    state: str
        Current ontological state (``Ego``, ``Jaz``, or ``Enotnost``).
    tension: float
        Current tension level influencing transitions.
    emotion: float
        Numerical representation of emotion intensity.
    emotion_label: str
        Descriptive label of the current emotion (e.g. ``strah``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "nevtralno"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity.
        label:
            Optional textual label describing the emotion.
        """
        self.emotion = value
        if label is not None:
            self.emotion_label = label
        # Emotional intensity increases tension and may trigger transitions
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        A transition from ``Ego`` -> ``Jaz`` or ``Jaz`` -> ``Enotnost`` occurs
        whenever :pyattr:`tension` exceeds ``0.7`` or :pyattr:`emotion` exceeds
        ``0.5``.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (Čustvo: {self.emotion_label})"
