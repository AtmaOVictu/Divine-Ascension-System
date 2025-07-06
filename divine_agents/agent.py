class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    def update_emotion(self, kind: str, value: float) -> None:
        """Update a specific emotion and adjust tension accordingly."""
        self.emotions[kind] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _dominant_emotion(self) -> float:
        return max(self.emotions.values())

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self._dominant_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        dominant = max(self.emotions, key=self.emotions.get)
        if self.emotions[dominant] > 0.5:
            return f"{base} (čustvo: {dominant})"
        return base
