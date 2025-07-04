from typing import List

from .agent import Agent

class Codex:
    """Central manager for ontological agents and their debates."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def register(self, agent: Agent) -> None:
        """Register an agent with the codex."""
        self.agents.append(agent)

    def debate(self, agent1: Agent, agent2: Agent) -> List[str]:
        """Conduct a debate between two agents and track transitions."""
        lines: List[str] = []
        # initial statements
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # update emotions which may trigger transitions
        agent1.update_emotion(0.6)
        agent2.update_emotion(0.8)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        # final statements after transition
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        return lines

