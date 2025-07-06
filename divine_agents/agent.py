class Agent:
    """Ontological agent capable of emotional transitions between states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = {e: 0.0 for e in self.EMOTIONS}
        self.emotion = emotion  # backward compatibility
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str = "anger") -> None:
        """Update a specific emotion intensity and adjust tension."""
        if emotion_type not in self.EMOTIONS:
            raise ValueError(f"Unknown emotion type: {emotion_type}")
        self.emotions[emotion_type] = value
        self.emotion = value  # keep highest recent value for legacy use
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self._max_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_prefix = self._emotion_prefix()
        if self.state == "Ego":
            return f"{emotion_prefix}Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{emotion_prefix}Resnica je relativna, oblikovana z našimi odnosi."
        return f"{emotion_prefix}Vse resnice so eno, medsebojno povezane."

    # ------------------------------------------------------------------
    # Internal helper methods
    # ------------------------------------------------------------------

    def _max_emotion(self) -> float:
        """Return the highest emotion intensity."""
        return max(self.emotions.values(), default=0.0)

    def _emotion_prefix(self) -> str:
        """Return a phrase reflecting the strongest emotion."""
        emotion, level = max(self.emotions.items(), key=lambda x: x[1])
        if level <= 0:
            return ""
        if emotion == "joy":
            return "Veselo, "
        if emotion == "fear":
            return "S strahom, "
        if emotion == "anger":
            return "Jezen, "
        return ""
