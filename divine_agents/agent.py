class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    EMOTION_EFFECTS = {
        "fear": 0.6,
        "joy": 0.4,
        "anger": 0.8,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.current_emotion = "neutral"
        self.history = [state]

    def feel(self, emotion: str, intensity: float) -> None:
        """Set the current emotion and adjust tension based on its intensity."""
        self.current_emotion = emotion
        self.emotion = intensity
        self.tension += intensity * self.EMOTION_EFFECTS.get(emotion, 0.0)

    def update_emotion(self, value: float) -> None:
        """Backward compatibility wrapper for adjusting emotion."""
        self.feel(self.current_emotion, value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
