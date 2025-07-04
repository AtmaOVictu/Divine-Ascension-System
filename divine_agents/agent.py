class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTION_IMPACT = {"fear": 0.3, "anger": 0.4, "joy": 0.1}

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value + self.EMOTION_IMPACT.get(emotion_type, 0)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def philosophical_principle(self) -> str:
        """Return the guiding principle of the agent's current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

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
        if self.state == "Ego":
            principle = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            principle = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            principle = "Vse resnice so eno, medsebojno povezane."
        return f"({self.emotion_type}) {principle}"
