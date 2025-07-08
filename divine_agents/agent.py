class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        # emotional intensities influencing tension
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.tension = 0.0
        self.history = [state]

    def update_emotion(self, emotion: str, value: float) -> None:
        """Set an emotion and recalculate tension."""
        if emotion not in self.emotions:
            raise ValueError(f"Unknown emotion '{emotion}'")
        self.emotions[emotion] = value
        self._recalculate_tension()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _recalculate_tension(self) -> None:
        """Recalculate tension based on current emotions."""
        # fear and anger raise tension, joy lowers it
        self.tension = max(0.0, (self.emotions["fear"] + self.emotions["anger"] - self.emotions["joy"]) / 2)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_peak = max(self.emotions.values())
        if self.tension > 0.7 or emotion_peak > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on current state and emotion."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotions["anger"] > 0.5:
            return f"{base} (Čutim jezo.)"
        if self.emotions["fear"] > 0.5:
            return f"{base} (Prežema me strah.)"
        if self.emotions["joy"] > 0.5:
            return f"{base} (Občutim veselje.)"
        return base
