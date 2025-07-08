class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: dict[str, float] = {}
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def set_emotion(self, kind: str, intensity: float) -> None:
        """Set or update an emotion and adjust tension."""
        self.emotions[kind] = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # State management
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        high_emotion = any(val > 0.5 for val in self.emotions.values())
        if self.tension > 0.7 or high_emotion:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Philosophy-aware responses
    # ------------------------------------------------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical answer that reflects the current state."""
        prefix = ""
        if self.emotions:
            e = max(self.emotions, key=self.emotions.get)
            if self.emotions[e] > 0.5:
                prefix = f"Občutim {e}. "

        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."

        return prefix + msg
