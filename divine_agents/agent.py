class Agent:
    """Represent an ontological agent with emotional state and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
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

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current emotion."""
        principle = self._state_principle()
        mood = self._emotion_label()
        return f"{principle} (feeling {mood})"

    # ------------------------------------------------------------------
    # Helper methods
    # ------------------------------------------------------------------
    def _emotion_label(self) -> str:
        if self.emotion > 0.7:
            return "anger"
        if self.emotion > 0.5:
            return "fear"
        if self.emotion > 0.3:
            return "curiosity"
        return "calm"

    def _state_principle(self) -> str:
        if self.state == "Ego":
            return "Truth is absolute and independent of others."
        if self.state == "Jaz":
            return "Truth is relative, shaped by our relationships."
        return "All truths are one, interconnected."
