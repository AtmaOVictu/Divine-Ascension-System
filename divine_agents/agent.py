class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent tracks simple emotional intensities that can raise its internal
    tension.  When either the tension exceeds ``0.7`` or the strongest emotion
    is above ``0.5`` a state transition occurs following the order
    ``Ego -> Jaz -> Enotnost``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotions: dict | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        # track emotional intensities individually
        base = {emotion: 0.0 for emotion in self.EMOTIONS}
        if emotions:
            base.update(emotions)
        self.emotions = base
        self.history = [state]

    def update_emotion(self, emotion: str, value: float) -> None:
        """Set an emotion intensity and adjust tension accordingly."""
        if emotion not in self.EMOTIONS:
            raise ValueError(f"Unknown emotion: {emotion}")
        self.emotions[emotion] = value
        self.tension += value

    @property
    def emotion_level(self) -> float:
        """Return the highest recorded emotion intensity."""
        return max(self.emotions.values())

    def dominant_emotion(self) -> str:
        """Return the name of the strongest emotion."""
        return max(self.emotions, key=self.emotions.get)

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

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_level > 0.5:
            emotion_info = f" Čutim {self.dominant_emotion()}."
        else:
            emotion_info = ""
        return base + emotion_info
