class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str = "neutral",
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def express_emotion(self, emotion_name: str, intensity: float) -> None:
        """Express an emotion that influences the agent's tension."""
        self.emotion_name = emotion_name
        self.update_emotion(intensity)

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

    def regulate(self) -> None:
        """Adjust tension and emotion to maintain balance."""
        if self.tension > 0.8:
            self.tension -= 0.1
        elif self.tension < 0.2:
            self.tension += 0.1
        if self.emotion > 0.8:
            self.emotion -= 0.1
        elif self.emotion < 0.2:
            self.emotion += 0.1

    def regenerate(self) -> None:
        """Reset emotional parameters to a neutral state."""
        self.emotion = 0.5
        self.tension = 0.5

    def modulate(self) -> None:
        """Check emotional levels and regenerate if needed."""
        if self.emotion > 0.7:
            self.regenerate()

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
