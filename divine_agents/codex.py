from typing import List
from .agent import Agent
from .modul import Modul


class Codex:
    """Central system managing agents and their interactions."""

    def __init__(self, agents: List[Agent] | None = None):
        self.agents: List[Agent] = agents or []
        self.modules: List[Modul] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def create_module(self, name: str, task: str) -> Modul:
        modul = Modul(name, task)
        for agent in self.agents:
            modul.add_agent(agent)
        self.modules.append(modul)
        return modul

    def simulate_step(self) -> List[str]:
        """Run a single dialogue step between the first two agents."""
        lines: List[str] = []
        if len(self.agents) < 2:
            return lines
        a1, a2 = self.agents[:2]
        lines.append(f"{a1.name} ({a1.state}): {a1.respond('Kaj je resnica?')}")
        lines.append(f"{a2.name} ({a2.state}): {a2.respond('Kaj je resnica?')}")

        a1.update_emotion(0.6)
        a2.update_emotion(0.8)
        a1.transition()
        a2.transition()
        lines.append(f"{a1.name} -> {a1.state}")
        lines.append(f"{a2.name} -> {a2.state}")
        return lines
