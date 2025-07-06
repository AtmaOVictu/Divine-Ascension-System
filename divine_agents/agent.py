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
        loyalty: float = 0.5,
        experiences: list | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.loyalty = loyalty
        self.experiences = experiences or []
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotional_state(self, state: str) -> None:
        """Set the current emotional state and adjust tension."""
        self.emotional_state = state
        self.adjust_tension_based_on_emotions()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def adjust_tension_based_on_emotions(self) -> None:
        """Modify tension based on emotional state."""
        if self.emotional_state == "angry":
            self.tension += 0.3
        elif self.emotional_state == "happy":
            self.tension -= 0.2
        else:
            self.tension += 0.1

    def add_experience(self, experience: str) -> None:
        """Record a new experience."""
        self.experiences.append(experience)

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


class MultiLayerTransitionSystem:
    """Advanced transition system considering multiple agent layers."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def multi_layer_transition(self) -> str:
        """Transition agent through multiple layers."""
        emotion_layer = self.agent.emotional_state
        tension_layer = self.agent.tension
        loyalty_layer = self.agent.loyalty
        experience_layer = (
            self.agent.experiences[-1] if self.agent.experiences else "neutral"
        )

        if emotion_layer == "fearful" and tension_layer > 0.7:
            self.agent.state = "Ego"
        elif loyalty_layer > 0.8 and emotion_layer == "happy":
            self.agent.state = "Jaz"
        elif "selfish" in experience_layer and tension_layer > 0.5:
            self.agent.state = "Enotnost"

        self.agent.history.append(self.agent.state)
        return self.agent.state
