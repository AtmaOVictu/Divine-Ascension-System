class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def _clamp(self, val: float) -> float:
        """Clamp a numeric value between 0 and 1."""
        return max(0.0, min(1.0, val))

    def update_emotion(self, value: float, accumulate: bool = False) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            New emotion value or increment when ``accumulate`` is ``True``.
        accumulate: bool, optional
            When ``True``, ``value`` is added to the current emotion instead of
            replacing it.
        """
        if accumulate:
            self.emotion += value
        else:
            self.emotion = value
        self.emotion = self._clamp(self.emotion)

        self.tension += value
        self.tension = self._clamp(self.tension)

    def update_tension(self, value: float) -> None:
        """Directly set tension level clamped between 0 and 1."""
        self.tension = self._clamp(value)

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
