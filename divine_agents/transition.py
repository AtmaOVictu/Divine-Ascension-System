from __future__ import annotations

from .agent import Agent


class MultiLayerTransitionSystem:
    """Handle complex transitions considering multiple factors."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def multi_layer_transition(self) -> str:
        emotion_layer = self.agent.emotion
        tension_layer = self.agent.tension
        loyalty_layer = self.agent.loyalty
        experience_layer = self.agent.experiences[-1] if self.agent.experiences else "neutral"

        if emotion_layer > 0.5 or tension_layer > 0.7:
            if self.agent.state == "Ego":
                self.agent.state = "Jaz"
            elif self.agent.state == "Jaz":
                self.agent.state = "Enotnost"

        self.agent.experiences.append(f"{self.agent.state}:{experience_layer}:{loyalty_layer}")
        return self.agent.state
