from __future__ import annotations
from .agent import Agent


class MultiLayerTransitionSystem:
    """Handle multi-dimensional transitions for an agent."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def multi_layer_transition(self) -> str:
        """Transition based on multiple layers of state."""
        emotion_layer = self.agent.emotional_state
        tension_layer = self.agent.tension
        loyalty_layer = self.agent.loyalty
        experience_layer = (
            self.agent.experiences[-1] if self.agent.experiences else "neutral"
        )

        if emotion_layer == "fearful" and tension_layer > 0.7:
            self.agent.state = "Ego"
        elif loyalty_layer > 0.8 and self.agent.emotion > 0.5:
            self.agent.state = "Jaz"
        elif "selfish" in experience_layer and tension_layer > 0.5:
            self.agent.state = "Enotnost"

        self.agent.history.append(self.agent.state)
        return self.agent.state


class ExperienceBasedLearning:
    """Simple experience based decision helper."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def learn_from_past_decisions(self, situation: str) -> str:
        if situation == "danger":
            if "helped" in self.agent.experiences:
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"


class HistoricalRefactor:
    """Refactor agent state based on historical keywords."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def auto_refactor(self) -> str:
        if "hesitation" in self.agent.history:
            self.agent.state = "Jaz"
        elif "self-preservation" in self.agent.history:
            self.agent.state = "Ego"
        return self.agent.state
