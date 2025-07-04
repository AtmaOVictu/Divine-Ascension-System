class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    @property
    def emotion_level(self) -> float:
        """Return the strongest emotion intensity."""
        return max(self.emotions.values()) if self.emotions else 0.0

    @property
    def dominant_emotion(self) -> str:
        """Return the name of the strongest emotion."""
        if not self.emotions:
            return ""
        return max(self.emotions, key=self.emotions.get)

    def update_emotion(self, name: str, intensity: float) -> None:
        """Update an emotion's intensity and adjust tension accordingly."""
        self.emotions[name] = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_note = ""
        if self.dominant_emotion and self.emotion_level > 0:
            emotion_note = f" (čutim {self.dominant_emotion})"

        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih.{emotion_note}"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z našimi odnosi.{emotion_note}"
        return f"Vse resnice so eno, medsebojno povezane.{emotion_note}"
