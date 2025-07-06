class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.tension = 0.0
        self.history = [state]

    def set_emotion(self, emotion: str, value: float) -> None:
        """Set intensity for a specific emotion and update tension."""
        if emotion in self.emotions:
            self.emotions[emotion] = value
            self.tension = sum(self.emotions.values())

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _emotion_level(self) -> float:
        """Return the highest intensity among emotions."""
        return max(self.emotions.values())

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self._emotion_level() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotions."""
        prefix = ""
        if self.emotions.get("anger", 0.0) > 0.5:
            prefix = "Z jezo, "
        elif self.emotions.get("fear", 0.0) > 0.5:
            prefix = "S strahom, "
        elif self.emotions.get("joy", 0.0) > 0.5:
            prefix = "Z veseljem, "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
