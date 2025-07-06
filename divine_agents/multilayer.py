class MultiLayerTransitionSystem:
    """Handle advanced state transitions considering multiple layers."""

    def __init__(self, agent):
        self.agent = agent

    def multi_layer_transition(self) -> str:
        emotion_layer = self.agent.emotion
        tension_layer = self.agent.tension
        loyalty_layer = self.agent.loyalty
        last_experience = self.agent.experiences[-1] if self.agent.experiences else "neutral"

        if self.agent.state == "Ego" and (tension_layer > 0.7 or emotion_layer > 0.5):
            self.agent.state = "Jaz"
        elif self.agent.state == "Jaz" and (loyalty_layer > 0.8 or "selfish" in last_experience):
            self.agent.state = "Enotnost"

        self.agent.history.append(self.agent.state)
        return self.agent.state
