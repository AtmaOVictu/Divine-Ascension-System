class Agent:
    """Ontological agent with emotional state and tension driven transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("neutral", "fear", "joy", "anger", "sadness", "confusion")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str = "neutral") -> None:
        """Set emotion intensity and label then adjust tension."""
        if name not in self.EMOTIONS:
            name = "neutral"
        self.emotion_name = name
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _emotion_prefix(self) -> str:
        """Return a textual prefix based on current emotion label."""
        return {
            "joy": "Z veseljem,",
            "anger": "Z jezo,",
            "fear": "S strahom,",
            "sadness": "Žalostno,",
            "confusion": "Zmedeno,",
        }.get(self.emotion_name, "Mirno,")

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
        """Return a philosophical answer shaped by state and emotion."""
        prefix = self._emotion_prefix()
        if self.state == "Ego":
            return f"{prefix} Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{prefix} Resnica je relativna, oblikovana z našimi odnosi."
        return f"{prefix} Vse resnice so eno, medsebojno povezane."
