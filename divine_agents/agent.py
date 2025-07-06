class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("anger", "joy", "sadness", "fear", "hope")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension = 0.0
        self.emotions = {e: 0.0 for e in self.EMOTIONS}
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion management
    # ------------------------------------------------------------------
    def update_emotion(self, emotion_name: str, value: float) -> None:
        """Update specific emotional state and check for transitions."""
        if emotion_name in self.emotions:
            self.emotions[emotion_name] += value
        self.update_tension_based_on_emotions()
        self.check_transition()

    def update_tension_based_on_emotions(self) -> None:
        """Recalculate tension as the average of all emotions."""
        self.tension = sum(self.emotions.values()) / len(self.emotions)

    def update_tension(self, value: float) -> None:
        """Directly set tension level and check for transition."""
        self.tension = value
        self.check_transition()

    # ------------------------------------------------------------------
    # Ontological transitions
    # ------------------------------------------------------------------
    def check_transition(self) -> None:
        """Check thresholds and trigger state transition."""
        if self.tension > 0.7 or any(v > 0.5 for v in self.emotions.values()):
            self.transition()

    def transition(self) -> str:
        """Perform state transition to the next ontological phase."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Philosophical response
    # ------------------------------------------------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class GradualAgent(Agent):
    """Agent supporting gradual emotional transitions."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.gradual_transition = False

    def update_emotion(self, emotion_name: str, value: float) -> None:
        """Gradually apply emotion and adjust state."""
        super().update_emotion(emotion_name, value)
        if self.tension > 0.5 and not self.gradual_transition:
            self.gradual_transition = True
            self.history.append("Gradual transition started")
        if self.gradual_transition:
            self.apply_gradual_change()

    def apply_gradual_change(self) -> None:
        """Simulate slow state changes based on accumulated tension."""
        if self.tension < 0.7:
            self.state = "Ego"
        elif self.tension < 1.0:
            self.state = "Jaz"
        else:
            self.state = "Enotnost"
        self.history.append(self.state)
