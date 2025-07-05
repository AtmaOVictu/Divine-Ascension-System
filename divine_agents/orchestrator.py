from __future__ import annotations
from typing import List
from .agent import Agent

class AgentDirigent:
    """Central coordinator that manages multiple agents."""

    def __init__(self, name: str):
        self.name = name
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Register an agent under the dirigent's guidance."""
        self.agents.append(agent)

    def direct_transition(self) -> None:
        """Direct each agent to transition if thresholds allow."""
        for agent in self.agents:
            agent.transition()

    def orchestrate(self) -> None:
        """Coordinate transitions for all agents."""
        self.direct_transition()


class Zbor:
    """Represents a collective group of agents."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def collective_consciousness(self) -> None:
        """Unify agents under a single state of 'Enotnost'."""
        for agent in self.agents:
            agent.state = "Enotnost"
            agent.history.append(agent.state)


class DivinitetniAgent(Agent):
    """Agent with a role of guiding others towards higher states."""

    def __init__(self, name: str):
        super().__init__(name, state="Enotnost")

    def elevate(self, agent: Agent) -> None:
        """Elevate another agent to 'Enotnost'."""
        agent.state = "Enotnost"
        agent.history.append(agent.state)

    def guide(self) -> str:
        return f"{self.name} vodi agenta skozi višje faze zavesti."
