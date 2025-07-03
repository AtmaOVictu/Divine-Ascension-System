class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            New emotion value in the range [0, 1].

        Raises
        ------
        ValueError
            If ``value`` is not within the allowed range.
        """
        if not 0 <= value <= 1:
            raise ValueError("Emotion value must be between 0 and 1.")
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value: float
            New tension value in the range [0, 1].

        Raises
        ------
        ValueError
            If ``value`` is not within the allowed range.
        """
        if not 0 <= value <= 1:
            raise ValueError("Tension value must be between 0 and 1.")
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
