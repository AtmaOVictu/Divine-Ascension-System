class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        # Map of emotion name to intensity
        self.emotions: dict[str, float] = {}
        self.history = [state]

    def _dominant_emotion(self) -> str | None:
        """Return the emotion with highest intensity if present."""
        if not self.emotions:
            return None
        return max(self.emotions, key=self.emotions.get)

    def update_emotion(self, value: float, kind: str = "generic") -> None:
        """Update a specific emotion and adjust tension."""
        self.emotions[kind] = value
        self.tension = sum(self.emotions.values())

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        max_emotion = max(self.emotions.values(), default=0)
        if self.tension > 0.7 or max_emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer including current emotional context."""
        emotion = self._dominant_emotion()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if emotion:
            return f"{base} (Čutim {emotion}.)"
        return base
