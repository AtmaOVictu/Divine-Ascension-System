class Agent:
    """Ontological agent capable of dynamic state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        key: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.key = key
        self.history = [state]
        self.activation_map = {
            "truth": "Ego",
            "negation": "Jaz",
            "wisdom": "Enotnost",
        }

    def update_emotion(self, value: float) -> None:
        """Increase emotion and adjust tension accordingly."""
        self.emotion += value
        self.tension += value
        self._check_activation()

    def update_tension(self, value: float) -> None:
        """Increase tension level."""
        self.tension += value
        self._check_activation()

    def transition(self) -> str:
        """Perform state transition according to thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _check_activation(self) -> None:
        """Automatically transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            self.transition()

    def set_key(self, key: str) -> None:
        """Set activation key and trigger state change if applicable."""
        self.key = key
        self.state = self.activation_map.get(key, self.state)
        self.history.append(self.state)

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        if self.emotion > 0.5:
            return f"{base} (izrazita custva: {self.emotion:.1f})"
        return base
