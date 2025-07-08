from .emotion import EmotionalBox


class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, language: str = "English", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.language = language
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.emotional_box = EmotionalBox(self, language)

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and adjust tension."""
        self.emotion = value
        self.tension += value
        self.emotional_box.update_emotion()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

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
        """Return an answer reflecting the agent's current ontological state."""
        if self.state == "Ego":
            return "Truth is absolute and independent of others."
        if self.state == "Jaz":
            return "Truth is relative, shaped by our relationships."
        return "All truths are one and interconnected."
