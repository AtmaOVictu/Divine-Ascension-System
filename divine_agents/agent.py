class Agent:
    """Ontological agent capable of transitioning between states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger", "neutral")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_intensity: float = 0.0, emotion: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_intensity = emotion_intensity
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion = emotion
        self.emotion_intensity = intensity
        self.tension += intensity

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
        """Return a philosophical answer depending on the state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        emotion_note = f" Občutim {self.emotion}." if self.emotion != "neutral" else ""
        return base + emotion_note
