class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        # Emotions represented as intensity values in range [0, 1]
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Set emotion intensity and adjust tension accordingly."""
        if emotion in self.emotions:
            self.emotions[emotion] = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or max(self.emotions.values()) > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion = max(self.emotions, key=self.emotions.get)
        addon = f" Čutim {emotion}." if self.emotions[emotion] > 0.3 else ""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + addon
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + addon
        return "Vse resnice so eno, medsebojno povezane." + addon
