class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.boxes = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self._check_extremes()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self._check_extremes()

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def create_box(self, name: str) -> None:
        """Record entry into a new ontological/emotional box."""
        self.boxes.append(name)

    def _check_extremes(self) -> None:
        """Create boxes when extreme emotion or tension values are reached."""
        if self.tension > 0.8:
            self.create_box("High Tension Box")
        elif self.tension < 0.2:
            self.create_box("Low Tension Box")

        if self.emotion > 0.8:
            self.create_box("High Emotion Box")
        elif self.emotion < 0.2:
            self.create_box("Low Emotion Box")
