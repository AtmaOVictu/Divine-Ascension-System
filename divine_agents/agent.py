class Agent:
    """Ontological agent that can transition between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension: float = 0.0
        self.emotion: float = 0.0
        self.emotion_name: str = "neutral"
        self.history = [state]

    def update_emotion(self, name: str, intensity: float) -> None:
        """Set emotion and increase tension accordingly."""
        self.emotion_name = name
        self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state if thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Dialogue utilities
    # ------------------------------------------------------------------
    def _principle(self) -> str:
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self) -> str:
        """Return a state dependent response influenced by emotion."""
        base = self._principle()
        if self.emotion_name != "neutral":
            return f"{base} Čutim {self.emotion_name}."
        return base
