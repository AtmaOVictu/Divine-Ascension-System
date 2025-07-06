class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = {e: 0.0 for e in self.EMOTIONS}
        self.history = [state]

    def set_emotion(self, name: str, value: float) -> None:
        """Set intensity for a specific emotion and adjust tension."""
        if name not in self.emotions:
            raise ValueError(f"Unknown emotion '{name}'")
        self.emotions[name] = value
        self.tension += value

    @property
    def emotion_level(self) -> float:
        """Return the maximum emotion intensity."""
        return max(self.emotions.values())

    def update_emotion(self, value: float) -> None:
        """Backward compatible wrapper that increases generic emotion."""
        self.set_emotion("joy", value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def dominant_emotion(self) -> str | None:
        """Return the emotion with the highest intensity or None."""
        if not any(self.emotions.values()):
            return None
        return max(self.emotions, key=self.emotions.get)

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        dominant = self.dominant_emotion()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if dominant:
            return f"{base} (\u010custvo: {dominant})"
        return base
