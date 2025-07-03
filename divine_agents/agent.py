class Agent:
    """Ontological agent capable of transitioning states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: dict[str, float] = emotions or {}
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion handling
    # ------------------------------------------------------------------
    def set_emotion(self, emotion: str, intensity: float) -> None:
        """Set an emotion with intensity and increase tension."""
        self.emotions[emotion] = intensity
        self.tension += intensity

    def max_emotion(self) -> float:
        """Return the highest emotion intensity."""
        return max(self.emotions.values(), default=0.0)

    # ------------------------------------------------------------------
    # State management
    # ------------------------------------------------------------------
    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.max_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Philosophical responses
    # ------------------------------------------------------------------
    def _current_emotion(self) -> str:
        if not self.emotions:
            return "brez čustev"
        return max(self.emotions, key=self.emotions.get)

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        prefix = f"({self._current_emotion()}) "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
