class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTION_EFFECT = {
        "fear": 1.0,
        "anger": 1.0,
        "joy": -0.5,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion type and intensity, adjusting tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        effect = self.EMOTION_EFFECT.get(emotion_type, 0.0)
        self.tension = max(0.0, self.tension + intensity * effect)

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
        """Return a philosophical answer depending on the current state and emotion."""
        emotion_note = f" Občutim {self.emotion_type}." if self.emotion_type != "neutral" else ""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + emotion_note
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + emotion_note
        return "Vse resnice so eno, medsebojno povezane." + emotion_note
