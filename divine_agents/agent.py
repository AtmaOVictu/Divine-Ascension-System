class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotions = {}
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update generic emotion intensity and adjust tension accordingly."""
        self.set_emotion("general", value)

    def set_emotion(self, kind: str, intensity: float) -> None:
        """Set a specific emotion and update overall tension."""
        self.emotions[kind] = intensity
        self.emotion = max(self.emotions.values())
        self.tension += intensity

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
        """Return a philosophical answer depending on the current state."""
        emotion_label = (
            max(self.emotions, key=self.emotions.get) if self.emotions else ""
        )
        suffix = f" (čustvo: {emotion_label})" if emotion_label else ""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + suffix
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + suffix
        return "Vse resnice so eno, medsebojno povezane." + suffix
