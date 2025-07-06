from .agent import Agent


class MultiLayerTransitionSystem:
    """Handle agent transitions using multiple influence layers."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def multi_layer_transition(self) -> str:
        """Transition through emotional, tension, loyalty and experience layers."""
        emotion_layer = self.agent.emotional_state
        tension_layer = self.agent.tension
        loyalty_layer = self.agent.loyalty
        experience_layer = (
            self.agent.experiences[-1] if self.agent.experiences else "neutral"
        )

        if self.agent.state == "Ego" and (
            tension_layer > 0.7 or emotion_layer == "fearful"
        ):
            self.agent.state = "Jaz"
        elif self.agent.state == "Jaz" and (
            loyalty_layer > 0.8 or "selfish" in experience_layer
        ):
            self.agent.state = "Enotnost"
        self.agent.history.append(self.agent.state)
        return self.agent.state
