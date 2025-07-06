class Agent:
    """Ontological agent capable of emotional transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension = 0.0
        # Expanded emotional spectrum
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
        """Update a specific emotional state and check for transitions."""
        if emotion_name in self.emotion:
            self.emotion[emotion_name] += value
        self._update_tension_based_on_emotions()
        self._check_transition()

    def _update_tension_based_on_emotions(self) -> None:
        """Calculate tension as the average intensity of all emotions."""
        self.tension = sum(self.emotion.values()) / len(self.emotion)

    def update_tension(self, value: float) -> None:
        """Directly set tension and check for possible transitions."""
        self.tension = value
        self._check_transition()

    # ------------------------------------------------------------------
    # Transition logic
    # ------------------------------------------------------------------
    def _check_transition(self) -> None:
        """Trigger a transition if tension or any emotion exceeds thresholds."""
        if self.tension > 0.7 or any(v > 0.5 for v in self.emotion.values()):
            self.transition()

    def transition(self) -> str:
        """Move the agent to the next ontological state."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        if not self.history or self.history[-1] != self.state:
            self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Responses
    # ------------------------------------------------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current state."""
        if self.state == "Ego":
            return f"{self.name} (Ego): Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{self.name} (Jaz): Resnica je relativna, oblikovana z našimi odnosi."
        return f"{self.name} (Enotnost): Vse resnice so eno, medsebojno povezane."


class GradualAgent(Agent):
    """Agent that experiences gradual emotional transitions."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.gradual_transition = False

    def update_emotion(self, emotion_name: str, value: float) -> None:
        """Apply emotion gradually, triggering state changes over time."""
        super().update_emotion(emotion_name, value)
        if self.tension > 0.5 and not self.gradual_transition:
            self.gradual_transition = True
            self.history.append("Gradual transition started")
        if self.gradual_transition:
            self._apply_gradual_change()

    def _apply_gradual_change(self) -> None:
        """Adjust state smoothly based on current tension."""
        if self.tension < 0.7:
            self.state = "Ego"
        elif self.tension < 1.0:
            self.state = "Jaz"
        else:
            self.state = "Enotnost"
        if self.history[-1] != self.state:
            self.history.append(self.state)
