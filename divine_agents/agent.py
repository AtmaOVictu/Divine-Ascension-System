class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        """Initialize the agent with a starting ontological state."""

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity and type, adjusting tension."""

        self.emotion = value
        self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""

        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _emotion_phrase(self) -> str:
        phrases = {
            "fear": "Občutim strah.",
            "joy": "Preveva me veselje.",
            "anger": "Preveva me jeza.",
            "sorrow": "Preveva me žalost.",
        }
        return phrases.get(self.emotion_type, "")

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state."""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        emotion = self._emotion_phrase()
        return f"{base} {emotion}".strip()
