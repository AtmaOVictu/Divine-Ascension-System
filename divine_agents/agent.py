class Agent:
    """Ontological agent able to transition between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # Keep track of state history for verification in tests
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

    def _emotion_descriptor(self) -> str:
        """Return a short text representing the emotional intensity."""
        if self.emotion > 0.6:
            return "strastno"
        if self.emotion > 0.3:
            return "negotovo"
        return "mirno"

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z nasimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        return f"{base} (odziv {self._emotion_descriptor()})"
