class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: How each emotion type influences tension
    EMOTION_MODIFIERS = {
        "fear": 0.5,
        "joy": 0.3,
        "anger": 0.7,
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

    def express_emotion(self, kind: str, intensity: float) -> None:
        """Apply an emotion which increases tension based on a modifier."""
        factor = self.EMOTION_MODIFIERS.get(kind, 0)
        self.emotion = intensity
        self.tension += intensity * factor
        self.transition()

    def _should_transition(self) -> bool:
        """Return True if transition thresholds are exceeded."""
        return self.tension > 0.7 or self.emotion > 0.5

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self._should_transition():
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

        prefix = "Mirno"
        if self.emotion > 0.5:
            prefix = "Čustveno" if self.tension <= 0.7 else "Strastno"

        return f"{prefix} odgovarjam: {base}"
