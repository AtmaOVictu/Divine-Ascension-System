class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_intensity: float = 0.0, emotion: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_intensity = emotion_intensity
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Update emotion type and intensity, adjusting tension."""
        self.emotion = emotion
        self.emotion_intensity = intensity
        # Emotions influence tension directly.
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition state if tension or emotion thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current state."""
        prefix = f"[{self.emotion}] " if self.emotion else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
