"""Advanced decision making and learning utilities for agents."""

from __future__ import annotations

import random
from typing import List

from .agent import Agent


class MultiLayerDecisionMaker:
    """Implements multi-dimensional decision making for an agent."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def multi_layer_decision(self) -> str:
        """Decide the next state based on emotion, tension and experiences."""
        emotional_layer = self.agent.emotion
        tension_layer = self.agent.tension
        history_layer = self.agent.experiences[-1] if self.agent.experiences else "neutral"

        if emotional_layer > 0.5 and tension_layer > 0.7:
            return self.agent.transition()
        if history_layer == "selfish" and tension_layer > 0.5:
            return self.agent.transition()
        return self.agent.state


class ExperienceBasedLearning:
    """Simple learning component that adapts behaviour based on experiences."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def learn_from_experience(self, situation: str) -> str:
        if situation == "danger":
            if "helped" in self.agent.experiences:
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"


class AgentGenerator:
    """Utility to generate agents with random properties."""

    def __init__(self, agent_type: str = "default") -> None:
        self.agent_type = agent_type

    def generate_agent(self) -> Agent:
        name = f"Agent_{random.randint(1, 1000)}"
        emotion = random.uniform(0, 1)
        tension = random.uniform(0, 1)
        loyalty = random.uniform(0, 1)

        if self.agent_type == "warrior":
            loyalty = min(1.0, loyalty + 0.2)
        elif self.agent_type == "healer":
            loyalty = max(0.0, loyalty - 0.2)

        return Agent(name, tension=tension, emotion=emotion, loyalty=loyalty)
