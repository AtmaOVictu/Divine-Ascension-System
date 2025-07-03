class Agent:
    """Ontological agent capable of emotional state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, intensity: float, emotion: str) -> None:
        """Update emotional intensity and name, adjusting tension."""
        self.emotion_level = intensity
        self.emotion = emotion
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return an answer shaped by state and emotion."""
        principles = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }
        mood = f"Občutim {self.emotion}. " if self.emotion != "neutral" else ""
        return mood + principles.get(self.state, "")
