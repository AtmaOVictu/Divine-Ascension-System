class Agent:
    """Represent an ontological agent capable of emotional transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: dict[str, float] = {}
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def apply_emotion(self, emotion: str, intensity: float) -> None:
        """Apply an emotion which increases tension."""
        self.emotions[emotion] = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set the current tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # State management
    # ------------------------------------------------------------------
    def _max_emotion(self) -> float:
        return max(self.emotions.values(), default=0.0)

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self._max_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Dialogue helpers
    # ------------------------------------------------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical answer based on state and emotion."""
        base = self.PHILOSOPHY[self.state]
        if not self.emotions:
            return base

        # choose the strongest emotion to influence the text
        emotion = max(self.emotions, key=self.emotions.get)
        prefix = {
            "fear": "(prestrašeno) ",
            "joy": "(veselo) ",
            "anger": "(jezno) ",
        }.get(emotion, f"({emotion}) ")
        return prefix + base
