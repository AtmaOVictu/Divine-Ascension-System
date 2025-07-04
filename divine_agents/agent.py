class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotions: dict | None = None,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update a specific emotion intensity and adjust tension accordingly."""
        if emotion not in self.emotions:
            self.emotions[emotion] = 0.0
        self.emotions[emotion] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        max_emotion = max(self.emotions.values(), default=0.0)
        if self.tension > 0.7 or max_emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotions."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotions.get("fear", 0.0) > 0.5:
            return base + " Moje srce je polno strahu."
        if self.emotions.get("joy", 0.0) > 0.5:
            return base + " To me navdaja z veseljem."
        if self.emotions.get("anger", 0.0) > 0.5:
            return base + " Čutim jezo."
        return base
