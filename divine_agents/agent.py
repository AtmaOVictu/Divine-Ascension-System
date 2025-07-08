class Agent:
    """Ontological agent capable of transitioning states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion_type: str = "neutral", emotion_intensity: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_type = emotion_type
        self.emotion_intensity = emotion_intensity
        self.history = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set emotion type and intensity and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion_intensity = intensity
        # Emotions like fear or anger are assumed to raise tension proportionally
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane."
        }[self.state]
        if self.emotion_type != "neutral":
            return f"({self.emotion_type}) {base}"
        return base
