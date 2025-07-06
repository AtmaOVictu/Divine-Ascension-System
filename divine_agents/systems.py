from __future__ import annotations
from typing import List

from .agent import Agent


class MultiLayerTransitionSystem:
    """Handle transitions considering multiple agent aspects."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def multi_layer_transition(self) -> str:
        """Determine next state based on emotion, tension, loyalty and history."""
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
        return self.agent.state


class ExperienceBasedLearning:
    """Simple decision making based on past experiences."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def learn_from_past_decisions(self, situation: str) -> str:
        if situation == "danger":
            if any("helped" in exp for exp in self.agent.experiences):
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"


class HistoricalRefactor:
    """Refactor agent state according to history."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def auto_refactor(self) -> str:
        history = self.agent.history
        if "hesitation" in history:
            self.agent.state = "Jaz"
        elif "self-preservation" in history:
            self.agent.state = "Ego"
        return self.agent.state


class EmotionalTensionDynamics:
    """Adjust tension based on current emotional state."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def adjust_tension_based_on_emotions(self) -> None:
        if self.agent.emotional_state == "angry":
            self.agent.tension += 0.3
        elif self.agent.emotional_state == "happy":
            self.agent.tension -= 0.2
        else:
            self.agent.tension += 0.1
