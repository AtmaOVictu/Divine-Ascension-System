"""Multi-layer decision making for agents."""

from .agent import Agent

class MultiLayerDecisionMaker:
    """Provide decisions based on multiple agent attributes."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def multi_layer_decision(self) -> str:
        """Return state transition advice based on multilayer analysis."""
        emotional_layer = self.agent.emotion
        tension_layer = self.agent.tension
        loyalty_layer = getattr(self.agent, "loyalty", 0.0)
        history_layer = self.agent.history

        if emotional_layer > 0.7 and tension_layer > 0.7:
            return "Prehod v Ego"
        if loyalty_layer > 0.8 and emotional_layer > 0.5:
            return "Prehod v Jaz"
        if "Ego" in history_layer and tension_layer > 0.5:
            return "Prehod v Enotnost"
        return self.agent.state
