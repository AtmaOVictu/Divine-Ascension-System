class Agent:
    """Ontological agent capable of transitioning states based on emotions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.history = [state]
        self.tension = 0.0
        # track different emotions influencing the agent
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update a specific emotion and adjust the agent's tension."""
        if emotion not in self.emotions:
            raise ValueError(f"Unknown emotion: {emotion}")
        self.emotions[emotion] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    @property
    def emotion_intensity(self) -> float:
        """Return the highest emotion intensity."""
        return max(self.emotions.values())

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, _: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
