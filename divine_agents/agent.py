class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions=None):
        self.name = name
        self.state = state
        self.tension = tension
        # emotions stored as a mapping of emotion name to intensity
        self.emotions = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update a specific emotion and adjust tension."""
        if emotion not in self.emotions:
            raise ValueError(f"Unknown emotion: {emotion}")
        self.emotions[emotion] = value
        self.tension = max(self.tension, value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    @property
    def emotion_level(self) -> float:
        """Aggregate emotion intensity for transition checks."""
        return max(self.emotions.values())

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotional_prefix = self._emotion_prefix()
        if self.state == "Ego":
            return f"{emotional_prefix}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{emotional_prefix}Resnica je relativna, oblikovana z našimi odnosi."
        return f"{emotional_prefix}Vse resnice so eno, medsebojno povezane."

    def _emotion_prefix(self) -> str:
        """Helper to generate an emotional prefix for responses."""
        dominant = max(self.emotions, key=self.emotions.get)
        level = self.emotions[dominant]
        if level <= 0.2:
            return ""
        if dominant == "fear":
            return "(v strahu) "
        if dominant == "anger":
            return "(jezno) "
        if dominant == "joy":
            return "(veselo) "
        return ""
