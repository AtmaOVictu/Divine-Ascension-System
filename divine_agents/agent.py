class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # Store a history of states for debugging and analysis
        self.history = [state]
        # Track individual emotions and their intensity
        self.emotions = {}

    def update_emotion(self, name: str, intensity: float) -> None:
        """Update a specific emotion and adjust tension accordingly."""
        intensity = max(0.0, min(1.0, intensity))
        self.emotions[name] = intensity
        self.emotion = intensity
        # emotions contribute directly to tension growth
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    def dominant_emotion(self) -> float:
        """Return the intensity of the strongest emotion."""
        if not self.emotions:
            return 0.0
        return max(self.emotions.values())

    def dominant_emotion_name(self) -> str:
        """Return the name of the strongest emotion or empty string."""
        if not self.emotions:
            return ""
        return max(self.emotions, key=self.emotions.get)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.dominant_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_note = self.dominant_emotion_name()
        prefix = f"({emotion_note}) " if emotion_note else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
