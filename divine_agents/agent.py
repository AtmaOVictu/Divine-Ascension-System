class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.tension = 0.0
        self.emotion = {"anger": 0.0, "joy": 0.0, "sadness": 0.0, "fear": 0.0}
        self.history = [state]

    def update_emotion(self, emotion_name: str, value: float) -> None:
        """Update a specific emotional state and adjust tension."""
        if emotion_name in self.emotion:
            self.emotion[emotion_name] += value
        self._update_tension_based_on_emotion()
        self.check_transition()

    def _update_tension_based_on_emotion(self) -> None:
        """Recalculate tension as the sum of all emotion values."""
        self.tension = sum(self.emotion.values())

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.check_transition()

    def check_transition(self) -> None:
        """Check if thresholds are exceeded and perform a transition."""
        if self.tension > 0.7 or any(v > 0.5 for v in self.emotion.values()):
            self.transition()

    def transition(self) -> str:
        """Change ontological state following the Ego -> Jaz -> Enotnost order."""
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


class GradualAgent(Agent):
    """Agent that moves gradually through states based on tension."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.gradual_transition = False

    def update_emotion(self, emotion_name: str, value: float) -> None:
        # High emotions trigger immediate transitions using base logic
        if value > 0.5 or (self.tension + value) > 0.7:
            super().update_emotion(emotion_name, value)
            return
        if emotion_name in self.emotion:
            self.emotion[emotion_name] += value
        self._update_tension_based_on_emotion()
        if self.tension >= 0.3 and not self.gradual_transition:
            self.gradual_transition = True
            self.history.append("Gradual transition started")
        if self.gradual_transition:
            self.apply_gradual_change()

    def apply_gradual_change(self) -> None:
        """Adjust state gradually based on current tension."""
        if self.tension < 0.3:
            self.state = "Ego"
        elif self.tension < 0.7:
            self.state = "Jaz"
        else:
            self.state = "Enotnost"
