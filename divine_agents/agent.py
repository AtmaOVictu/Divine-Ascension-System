class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotions: dict | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    def set_emotion(self, emotion: str, value: float) -> None:
        """Set an emotion level and adjust tension."""
        if emotion not in self.emotions:
            raise ValueError(f"Unsupported emotion: {emotion}")
        self.emotions[emotion] = value
        self.tension = max(self.tension, value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        max_emotion = max(self.emotions.values())
        if self.tension > 0.7 or max_emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = self.PHILOSOPHY[self.state]
        mood = ""
        if self.emotions.get("fear", 0.0) > 0.5:
            mood = "(v strahu)"
        elif self.emotions.get("anger", 0.0) > 0.5:
            mood = "(jezno)"
        elif self.emotions.get("joy", 0.0) > 0.5:
            mood = "(veselo)"
        return f"{base} {mood}".strip()
