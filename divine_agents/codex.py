import random
from typing import Dict, List
from .agent import Agent
from .knowledge_base import KnowledgeBase
from .modul import Modul
from .dialogue import philosophical_dialogue


class Codex:
    """Central system orchestrating agents and modules."""

    def __init__(self, num_agents: int = 3):
        self.agents: List[Agent] = []
        self.modules: List[Modul] = []
        self.knowledge_base = KnowledgeBase()
        self._init_agents(num_agents)
        self._init_modules()

    def _init_agents(self, count: int) -> None:
        for i in range(count):
            name = f"Agent{i+1}"
            self.add_agent(name)

    def _init_modules(self) -> None:
        tasks = ["samospoznanje", "logični prehod", "emotivni prehod"]
        for idx, task in enumerate(tasks, 1):
            modul = Modul(f"Modul {idx}", task)
            for agent in self.agents:
                modul.add_agent(agent)
            self.modules.append(modul)

    def add_agent(self, name: str) -> None:
        agent = Agent(name)
        self.agents.append(agent)

    def simulate_interaction(self) -> List[str]:
        if len(self.agents) < 2:
            return []
        a1, a2 = random.sample(self.agents, 2)
        return philosophical_dialogue(a1, a2)

    def system_state(self) -> Dict[str, str]:
        return {a.name: a.state for a in self.agents}
