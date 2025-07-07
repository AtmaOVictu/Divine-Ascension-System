class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions=None):
        self.name = name
        self.state = state
        self.tension = tension
        # track multiple emotions for compound states
        self.emotions = emotions or {"joy": 0.0, "fear": 0.0, "anger": 0.0}
        self.history = [state]

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update a specific emotion intensity and adjust tension accordingly."""
        if emotion not in self.emotions:
            self.emotions[emotion] = 0.0
        self.emotions[emotion] = value
        self.tension += value

    @property
    def overall_emotion(self) -> float:
        """Return the dominant emotion intensity."""
        if not self.emotions:
            return 0.0
        return max(self.emotions.values())

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.overall_emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        # emotional tone influences the response
        dominant = max(self.emotions, key=self.emotions.get)
        if self.emotions[dominant] > 0.5:
            base += f" Čutim {dominant}."
        return base
