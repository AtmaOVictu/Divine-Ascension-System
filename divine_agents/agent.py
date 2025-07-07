class Agent:
    """Ontological agent capable of emotional state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    RESPONSES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and increase tension accordingly."""
        self.emotion = value
        # Tension grows with emotion but is capped between 0 and 1
        self.tension = min(1.0, self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level (clamped between 0 and 1)."""
        self.tension = max(0.0, min(1.0, value))

    # ------------------------------------------------------------------
    # State transitions and responses
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Transition between ontological states if thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion."""
        base = self.RESPONSES.get(self.state, "")
        if self.emotion > 0.7:
            return f"{base} Čutim to zelo močno."  # emotional response
        if self.emotion < 0.3:
            return f"{base} To povem mirno."  # calm response
        return base
