class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    def feel(self, emotion: str, intensity: float) -> None:
        """Set an emotional intensity and adjust tension."""
        if emotion not in self.emotions:
            raise ValueError(f"Unknown emotion: {emotion}")
        self.emotions[emotion] = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    @property
    def emotion(self) -> float:
        """Aggregate emotion value."""
        return max(self.emotions.values())

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
        """Return a philosophical answer influenced by state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotions.get("fear", 0) > 0.5:
            base += " Čutim strah."
        elif self.emotions.get("anger", 0) > 0.5:
            base += " Čutim jezo."
        elif self.emotions.get("joy", 0) > 0.5:
            base += " Preveva me veselje."
        return base
