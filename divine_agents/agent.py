class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension = 0.0
        # Track multiple emotions to allow nuanced state changes
        self.emotion = {
            "anger": 0.0,
            "joy": 0.0,
            "sadness": 0.0,
            "fear": 0.0,
        }
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def update_emotion(self, emotion_name: str, value: float) -> None:
        """Update a specific emotional state and adjust tension."""
        if emotion_name in self.emotion:
            self.emotion[emotion_name] += value
            if self.emotion[emotion_name] < 0:
                self.emotion[emotion_name] = 0.0
        self.update_tension_based_on_emotion()
        self.check_transition()

    def update_tension_based_on_emotion(self) -> None:
        """Calculate tension from the sum of all emotional intensities."""
        self.tension = sum(self.emotion.values())

    def update_tension(self, value: float) -> None:
        """Directly set tension level and check for possible transition."""
        self.tension = value
        self.check_transition()

    # ------------------------------------------------------------------
    # State management
    # ------------------------------------------------------------------
    def check_transition(self) -> None:
        """Check if thresholds are met and transition to the next state."""
        if self.tension > 0.7 or any(v > 0.5 for v in self.emotion.values()):
            self.transition()

    def transition(self) -> str:
        """Perform the state transition."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Philosophical response
    # ------------------------------------------------------------------
    def respond(self, question: str = "") -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return f"{self.name} (Ego): Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{self.name} (Jaz): Resnica je relativna, oblikovana z našimi odnosi."
        return f"{self.name} (Enotnost): Vse resnice so eno, medsebojno povezane."


class GradualAgent(Agent):
    """Agent that transitions states gradually based on tension."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.gradual_transition = False

    def update_emotion(self, emotion_name: str, value: float) -> None:
        prev_state = self.state
        super().update_emotion(emotion_name, value)
        if self.tension > 0.5 and not self.gradual_transition:
            self.gradual_transition = True
            self.history.append("Gradual transition started")
        if self.gradual_transition and self.state == prev_state:
            self.apply_gradual_change()

    def apply_gradual_change(self) -> None:
        """Slowly change state depending on current tension level."""
        previous_state = self.state
        if self.state == "Ego" and self.tension >= 0.7:
            self.state = "Jaz"
        elif self.state == "Jaz" and self.tension >= 1.0:
            self.state = "Enotnost"
        if previous_state != self.state:
            self.history.append(self.state)
