from .agent import Agent

class OppositeAgent(Agent):
    """Agent that can switch to the opposite ontological state."""

    OPPOSITES = {
        "Ego": "Jaz",
        "Jaz": "Ego",
        "Enotnost": "Jaz",
    }

    def activate_opposite_state(self) -> str:
        """Switch to the opposite state defined in OPPOSITES."""
        self.state = self.OPPOSITES.get(self.state, self.state)
        self.history.append(self.state)
        return self.state

    def contradiction_transition(self, emotion_increment: float = 0.0) -> str:
        """Increase emotion, update tension, and transition if thresholds are met."""
        self.update_emotion(emotion_increment)
        if self.tension > 0.7 or self.emotion > 0.5:
            return self.activate_opposite_state()
        self.history.append(self.state)
        return self.state
