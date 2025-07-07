class Agent:
    """An ontological agent capable of transitioning philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger", "sorrow")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension: float = 0.0
        # store emotional intensities e.g. {"fear": 0.3}
        self.emotions: dict[str, float] = {}
        self.history = [state]

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Set an emotion and update tension accordingly."""
        if emotion not in self.EMOTIONS:
            raise ValueError(f"Unknown emotion: {emotion}")
        self.emotions[emotion] = intensity
        self.tension = min(1.0, self.tension + intensity)

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    @property
    def emotion_intensity(self) -> float:
        """Return the highest emotional intensity."""
        return max(self.emotions.values() or [0.0])

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceeds thresholds."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by ontological state."""
        fear = self.emotions.get("fear", 0)
        anger = self.emotions.get("anger", 0)
        joy = self.emotions.get("joy", 0)

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if fear > 0.5:
            base = f"S strahom poudarjam, da {base.lower()}"
        elif anger > 0.5:
            base = f"Z jezo trdim, da {base.lower()}"
        elif joy > 0.5:
            base = f"Z veseljem verjamem, da {base.lower()}"
        return base

