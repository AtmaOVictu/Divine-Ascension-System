from __future__ import annotations
import random
from typing import List

from .agent import Agent


class MultiLayerDecisionMaker:
    """Make decisions based on multiple agent layers."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def decide(self) -> str:
        emotional_layer = self.agent.emotion
        tension_layer = self.agent.tension
        loyalty_layer = self.agent.loyalty
        history_layer = self.agent.experiences

        if loyalty_layer > 0.8 and emotional_layer > 0.5:
            self.agent.state = "Jaz"
        elif history_layer and "selfish" in history_layer[-1] and tension_layer > 0.5:
            self.agent.state = "Enotnost"
        elif emotional_layer > 0.7 and tension_layer > 0.7:
            self.agent.state = "Ego"

        self.agent.history.append(self.agent.state)
        return self.agent.state


class ExperienceBasedLearning:
    """Simple learning mechanism based on past experiences."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def learn(self, situation: str) -> str:
        if situation == "danger":
            if "helped" in self.agent.experiences:
                decision = "Act selflessly"
                self.agent.loyalty += 0.1
            else:
                decision = "Self-preservation"
                self.agent.loyalty -= 0.1
        else:
            decision = "Neutral decision"
        return decision


class AgentGenerator:
    """Generate agents with random properties."""

    def __init__(self, agent_type: str = "default"):
        self.agent_type = agent_type

    def generate_agent(self) -> Agent:
        name = f"Agent_{random.randint(1, 1000)}"
        emotion = random.random()
        loyalty = random.uniform(0, 1)
        tension = random.uniform(0, 1)

        if self.agent_type == "warrior":
            loyalty = min(loyalty + 0.2, 1)
        elif self.agent_type == "healer":
            loyalty = max(loyalty - 0.2, 0)

        return Agent(name, tension=tension, emotion=emotion, loyalty=loyalty)
