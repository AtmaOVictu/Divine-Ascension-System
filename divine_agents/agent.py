class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: dict[str, float] = emotions or {}
        self.history = [state]

    @property
    def emotion_intensity(self) -> float:
        """Return the highest recorded emotion intensity."""
        return max(self.emotions.values(), default=0.0)

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update a specific emotion and increase tension accordingly."""
        self.emotions[emotion] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        dominant = None
        if self.emotions:
            dominant = max(self.emotions, key=self.emotions.get)
        mood = f" Čutim {dominant}." if dominant else ""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + mood
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + mood
        return "Vse resnice so eno, medsebojno povezane." + mood
