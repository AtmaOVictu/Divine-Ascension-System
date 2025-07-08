class Agent:
    """Ontological agent capable of changing state based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension = 0.0
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def update_emotion(self, emotion: str, value: float) -> None:
        """Set an emotion value and adjust tension if the value increases."""
        prev = self.emotions.get(emotion, 0.0)
        self.emotions[emotion] = value
        if value > prev:
            self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # State transitions
    # ------------------------------------------------------------------
    def _emotion_intensity(self) -> float:
        """Return the strongest emotion value."""
        return max(self.emotions.values())

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self._emotion_intensity() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Philosophical behaviour
    # ------------------------------------------------------------------
    def philosophical_principle(self) -> str:
        """Return the core philosophical statement for the current state."""
        if self.state == "Ego":
            return "Truth is absolute and independent of others."
        if self.state == "Jaz":
            return "Truth is relative and shaped by our relationships."
        return "All truths are one and interconnected."

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotions."""
        base = self.philosophical_principle()
        if self.emotions.get("anger", 0) > 0.5:
            return base + " (spoken with anger)"
        if self.emotions.get("joy", 0) > 0.5:
            return base + " (joyfully)"
        if self.emotions.get("fear", 0) > 0.5:
            return base + " (with hesitation)"
        return base
