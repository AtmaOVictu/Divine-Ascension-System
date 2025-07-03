class Agent:
    """Represents an ontological agent capable of transitioning states.

    State transitions are driven by ``tension`` and ``emotion`` values. When
    either ``tension`` exceeds ``0.7`` or ``emotion`` exceeds ``0.5`` the agent
    advances from ``Ego`` → ``Jaz`` → ``Enotnost``.  Responses include a short
    emotional descriptor so tests can verify that emotion influences output.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def _emotion_label(self) -> str:
        """Return a short textual representation of current emotion level."""
        if self.emotion > 0.8:
            return "z veliko strastjo"
        if self.emotion > 0.5:
            return "\u010dustveno"
        return "mirno"

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

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} ({self._emotion_label()})"
