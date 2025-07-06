class DecisionMaker:
    """Decision-making engine that considers emotions, tension, loyalty and history."""

    def __init__(self, agent):
        self.agent = agent

    def decide_transition(self) -> str:
        """Return the next state based on agent's context."""
        if self.agent.emotion_label == "fearful" and self.agent.loyalty < 0.5:
            return "Ego"
        elif self.agent.loyalty > 0.7 and self.agent.emotion_label == "happy":
            return "Jaz"
        elif self.agent.tension > 0.7 or self.agent.emotion > 0.5 or self.agent.emotion_label == "sad":
            if self.agent.state == "Ego":
                return "Jaz"
            return "Enotnost"
        else:
            if "Ego" in self.agent.history[-3:]:
                return "Jaz"
            return self.agent.state
