from __future__ import annotations

"""Additional systems providing dynamic behaviour for agents."""

from typing import List

from .agent import Agent


class EmotionalTensionDynamics:
    """Adjust an agent's tension based on its emotional state."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def adjust_tension_based_on_emotions(self) -> None:
        if self.agent.emotional_state == "angry":
            self.agent.tension += 0.3
        elif self.agent.emotional_state == "happy":
            self.agent.tension -= 0.2
        else:
            self.agent.tension += 0.1


class MultiLayerTransitionSystem:
    """Perform transitions using several agent attributes."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def multi_layer_transition(self) -> str:
        emotion_layer = self.agent.emotional_state
        tension_layer = self.agent.tension
        loyalty_layer = self.agent.loyalty
        experience_layer = self.agent.experiences[-1] if self.agent.experiences else ""

        if emotion_layer == "fearful" and tension_layer > 0.7:
            self.agent.state = "Ego"
        elif loyalty_layer > 0.8 and emotion_layer == "happy":
            self.agent.state = "Jaz"
        elif "selfish" in experience_layer and tension_layer > 0.5:
            self.agent.state = "Enotnost"

        self.agent.history.append(self.agent.state)
        return self.agent.state


class ExperienceBasedLearning:
    """A very small experience based decision helper."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def learn_from_past_decisions(self, situation: str) -> str:
        if situation == "danger":
            if "helped" in self.agent.experiences:
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"


class HistoricalRefactor:
    """Adjust agent state using its historical data."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def auto_refactor(self) -> str:
        if "hesitation" in self.agent.history:
            self.agent.state = "Jaz"
        elif "self-preservation" in self.agent.history:
            self.agent.state = "Ego"
        return self.agent.state
