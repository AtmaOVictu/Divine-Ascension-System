class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        # store emotions as a mapping from emotion type to intensity
        self.emotions: dict[str, float] = {}
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def update_emotion(self, emotion: str, value: float) -> None:
        """Update a specific emotion and adjust tension accordingly."""
        self.emotions[emotion] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _max_emotion(self) -> float:
        """Return the highest recorded emotion intensity."""
        return max(self.emotions.values(), default=0.0)

    # ------------------------------------------------------------------
    # State transitions
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self._max_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Dialogue
    # ------------------------------------------------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if not self.emotions:
            return base

        # Influence of dominant emotion on response
        emotion = max(self.emotions, key=self.emotions.get)
        if emotion == "fear":
            return f"{base} Čutim strah."
        if emotion == "anger":
            return f"{base} Čutim jezo."
        if emotion == "joy":
            return f"{base} Čutim veselje."
        return base

