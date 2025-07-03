import random
from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue
from .sozvocje import Sozvocje


class Codex:
    """Container managing agents and conceptual relations."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []
        self.sozvocje = Sozvocje()

    def add_agent(self, name: str, emotion: float = 0.0) -> Agent:
        agent = Agent(name)
        if emotion:
            agent.update_emotion(emotion)
        self.agents.append(agent)
        return agent

    def add_concept(self, name: str, color: str, description: str) -> None:
        self.sozvocje.add_node(name, color, description)

    def connect_concepts(self, n1: str, n2: str) -> None:
        self.sozvocje.add_edge(n1, n2)

    def generate_input(self, content: str) -> str:
        return f"00 11 RESNICAMI: {content}"

    def simulate_interaction(self) -> str:
        if len(self.agents) < 2:
            return "Premalo agentov za interakcijo."
        a1, a2 = random.sample(self.agents, 2)
        return a1.interact(a2)

    def dialogue(self, a1: Agent, a2: Agent) -> List[str]:
        return philosophical_dialogue(a1, a2)
