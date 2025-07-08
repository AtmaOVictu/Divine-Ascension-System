class Agent:
    """Ontological agent capable of emotional state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion management
    # ------------------------------------------------------------------
    def update_emotion(self, emotion: str, value: float) -> None:
        """Set emotion intensity (0-1) and increase tension."""
        value = max(0.0, min(1.0, value))
        self.emotions[emotion] = value
        # tension grows with emotional intensity
        self.tension = min(1.0, self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level (0-1)."""
        self.tension = max(0.0, min(1.0, value))

    # ------------------------------------------------------------------
    # Transition logic
    # ------------------------------------------------------------------
    def _max_emotion(self) -> float:
        """Return the highest emotion intensity."""
        return max(self.emotions.values())

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self._max_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Philosophical responses
    # ------------------------------------------------------------------
    def _emotion_prefix(self) -> str:
        """Return a prefix representing the dominant emotion."""
        dominant = max(self.emotions, key=self.emotions.get)
        intensity = self.emotions[dominant]
        if intensity <= 0.5:
            return ""
        translations = {"fear": "S strahom", "joy": "Z veseljem", "anger": "Z jezo"}
        return f"{translations.get(dominant, '')} " if translations.get(dominant) else ""

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = self._emotion_prefix()
        if self.state == "Ego":
            return f"{prefix}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{prefix}Resnica je relativna, oblikovana z našimi odnosi."
        return f"{prefix}Vse resnice so eno, medsebojno povezane."
