class Agent:
    """Ontological agent capable of emotional transitions between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: dict[str, float] = emotions or {}
        self.history = [state]

    def set_emotion(self, name: str, value: float) -> None:
        """Set an emotion intensity and adjust tension accordingly."""
        self.emotions[name] = value
        if name in {"fear", "anger"}:
            self.tension += value
        elif name == "joy":
            self.tension = max(0.0, self.tension - value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_trigger = any(v > 0.5 for v in self.emotions.values())
        if self.tension > 0.7 or emotion_trigger:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotions."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotions:
            dominant = max(self.emotions, key=self.emotions.get)
            if self.emotions[dominant] > 0.5:
                base = f"({dominant}) " + base
        return base
