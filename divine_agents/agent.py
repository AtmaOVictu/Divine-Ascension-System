class Agent:
    """Ontological agent capable of transitioning states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger", "sorrow", "neutral")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity, optionally setting its name, and adjust tension."""
        self.emotion = value
        if name:
            self.emotion_name = name
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _emotion_prefix(self) -> str:
        """Return a prefix describing the agent's current emotional state."""
        prefixes = {
            "fear": "V strahu",
            "joy": "Z veseljem",
            "anger": "S jezo",
            "sorrow": "S žalostjo",
            "neutral": "Mirno",
        }
        return prefixes.get(self.emotion_name, "Mirno")

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by ontological state and emotion."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{self._emotion_prefix()} povem: {base}"
