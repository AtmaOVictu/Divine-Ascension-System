class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Agent identifier.
    state: str, optional
        Initial ontological state. Defaults to ``"Ego"``.
    tension: float, optional
        Initial tension level.
    emotion: float, optional
        Initial emotion intensity.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    _MOODS = {
        "low": "mirno",
        "medium": "resno",
        "high": "razburjeno",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
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

    # ------------------------------------------------------------------
    # Dialogue helpers
    # ------------------------------------------------------------------

    def mood(self) -> str:
        """Return a textual representation of the agent's current mood."""
        if self.emotion > 0.7:
            return self._MOODS["high"]
        if self.emotion > 0.3:
            return self._MOODS["medium"]
        return self._MOODS["low"]

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        mood = self.mood()
        if self.state == "Ego":
            return f"[{mood}] Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"[{mood}] Resnica je relativna, oblikovana z našimi odnosi."
        return f"[{mood}] Vse resnice so eno, medsebojno povezane."
