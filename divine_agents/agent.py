class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotions: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    @property
    def emotion(self) -> float:
        """Return the dominant emotion intensity."""
        return max(self.emotions.values()) if self.emotions else 0.0

    def update_emotion(self, emotion: str, value: float) -> None:
        """Set an emotion intensity and adjust tension."""
        self.emotions[emotion] = value
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
        """Return a philosophical answer depending on state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        dominant = max(self.emotions, key=self.emotions.get)
        mood = ""
        if self.emotions[dominant] > 0.5:
            mood_word = {
                "fear": "prestrašeno",
                "joy": "veselo",
                "anger": "jezno",
            }.get(dominant, "")
            mood = f" ({mood_word})"
        return base + mood
