class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTION_DESCRIPTORS = {
        "fear": "prestrašeno",
        "anger": "jezno",
        "joy": "veselo",
        "neutral": "mirno",
    }

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity, type and adjust tension."""
        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def emotion_descriptor(self) -> str:
        """Return a short descriptor based on the current emotion type."""
        return self.EMOTION_DESCRIPTORS.get(self.emotion_type, "")

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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        desc = self.emotion_descriptor()
        if desc:
            return f"{desc} {base}"
        return base
