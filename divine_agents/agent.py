class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Agent identifier.
    state: str, optional
        Initial ontological state, default ``"Ego"``.
    tension: float, optional
        Starting tension value.
    emotion: float, optional
        Starting emotion intensity.
    emotion_label: str, optional
        Descriptive label of the current emotion (``"neutral"`` by default).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral") -> None:
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
            Optional descriptive label for the emotion.
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
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def __str__(self) -> str:
        return f"{self.name}({self.state}, {self.emotion_label}, T={self.tension:.2f})"

    @property
    def philosophical_principle(self) -> str:
        """Return the core philosophical principle of the current state."""
        if self.state == "Ego":
            return "absolute"
        if self.state == "Jaz":
            return "relative"
        return "unified"
