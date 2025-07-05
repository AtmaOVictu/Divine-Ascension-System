class Agent:
    """Ontological agent capable of transitioning through philosophical states.

    Parameters are clamped between 0 and 1 to keep emotion and tension in
    reasonable bounds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state if state in self.STATES else "Ego"
        self.tension = self._clamp(tension)
        self.emotion = self._clamp(emotion)
        self.history = [self.state]

    @staticmethod
    def _clamp(value: float) -> float:
        """Clamp ``value`` to the ``0..1`` interval."""
        return max(0.0, min(1.0, value))

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = self._clamp(value)
        self.tension = self._clamp(self.tension + self.emotion)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
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
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Moja čustva so močna."
        return base
