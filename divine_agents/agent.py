class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        # Track basic emotions that influence tension
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.tension = 0.0
        self.history = [state]

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update a specific emotion and recompute tension."""
        if emotion not in self.emotions:
            self.emotions[emotion] = 0.0
        self.emotions[emotion] = value
        self.tension = sum(self.emotions.values())

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def dominant_emotion(self) -> str:
        """Return the emotion with the highest intensity."""
        return max(self.emotions, key=self.emotions.get)

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
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        return f"{base} (\u010dustvo: {self.dominant_emotion()})"
