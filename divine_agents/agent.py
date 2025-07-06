class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotions: dict | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotions: dict[str, float] = emotions or {}
        self.history = [state]

    def update_emotion(self, value: float, name: str = "generic") -> None:
        """Update a named emotion intensity and adjust tension accordingly."""
        self.emotions[name] = value
        self.emotion = value
        self.tension += value

    def get_dominant_emotion(self) -> str | None:
        """Return the name of the emotion with highest intensity."""
        if not self.emotions:
            return None
        return max(self.emotions, key=self.emotions.get)

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

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by state and emotions."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_phrases = {
            "fear": "s strahom",
            "joy": "z veseljem",
            "anger": "z jezo",
        }
        dominant = self.get_dominant_emotion()
        suffix = f" ({emotion_phrases[dominant]})" if dominant in emotion_phrases else ""
        return f"{base}{suffix}"
