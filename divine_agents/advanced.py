"""Advanced decision-making and learning for ontological agents."""
from __future__ import annotations

import random
from typing import List

from .agent import Agent


class MultiLayerDecisionMaker:
    """Handle multi-layer decision-making for a given agent."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def multi_layer_decision(self) -> str:
        """Return the next state based on several factors."""
        emotional_layer = self.agent.emotion
        tension_layer = self.agent.tension
        loyalty_layer = getattr(self.agent, "loyalty", 0.0)
        history_layer = self.agent.history

        if emotional_layer > 0.5 or tension_layer > 0.7:
            return self.agent.transition()
        if loyalty_layer > 0.8 and emotional_layer > 0.5:
            return self.agent.transition()
        if "selfish" in history_layer and tension_layer > 0.5:
            return self.agent.transition()
        return self.agent.state


class ExperienceBasedLearning:
    """Simple learning mechanism relying on previous experiences."""

    def __init__(self, agent: Agent):
        self.agent = agent
        self.history = agent.history

    def learn_from_experience(self, situation: str) -> str:
        """Derive action from experience."""
        if situation == "danger":
            if "helped" in self.history:
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"


class AgentGenerator:
    """Generate agents with randomised attributes."""

    def __init__(self, agent_type: str = "default"):
        self.agent_type = agent_type

    def generate_agent(self) -> Agent:
        name = f"Agent_{random.randint(1, 100)}"
        emotional_state = random.uniform(0, 1)
        loyalty = random.uniform(0, 1)

        agent = Agent(name, emotion=emotional_state)
        agent.loyalty = loyalty

        if self.agent_type == "warrior":
            agent.loyalty = min(agent.loyalty + 0.2, 1.0)
        elif self.agent_type == "healer":
            agent.loyalty = max(agent.loyalty - 0.2, 0.0)

        return agent
