class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotional_state: str = "neutral",
        loyalty: float = 0.0,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.loyalty = loyalty
        self.experiences: list[str] = []
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def add_experience(self, experience: str) -> None:
        """Record an experience in the agent's history."""
        self.experiences.append(experience)

    def adjust_tension_based_on_emotions(self) -> None:
        """Modify tension according to the current emotional state."""
        if self.emotional_state == "angry":
            self.tension += 0.3
        elif self.emotional_state == "happy":
            self.tension -= 0.2
        else:
            self.tension += 0.1

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def multi_layer_transition(self) -> str:
        """Complex transition considering loyalty and experiences."""
        emotion_layer = self.emotional_state
        tension_layer = self.tension
        loyalty_layer = self.loyalty
        experience_layer = self.experiences[-1] if self.experiences else "neutral"

        if emotion_layer == "fearful" and tension_layer > 0.7:
            self.state = "Ego"
        elif loyalty_layer > 0.8 and emotion_layer == "happy":
            self.state = "Jaz"
        elif "selfish" in experience_layer and tension_layer > 0.5:
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
