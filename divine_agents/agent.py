class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: Mapping of emotion labels to their base intensity.
    EMOTION_LEVELS = {
        "fear": 0.4,
        "anger": 0.6,
        "joy": 0.3,
    }

    def __init__(
        self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        # clamp the emotion between 0 and 1 for stability
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def apply_emotion(self, label: str) -> None:
        """Apply an emotion by label, affecting internal tension."""
        intensity = self.EMOTION_LEVELS.get(label, 0.0)
        self.update_emotion(intensity)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

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
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            return f"{base} Čutim močna čustva, ki me vodijo."
        if self.emotion > 0.4:
            return f"{base} Moja čustva se krepijo."
        return base
