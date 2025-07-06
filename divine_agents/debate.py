"""Module providing a debate simulation between two ontological agents."""

from typing import List

from .agent import Agent

class PhilosophicalDebate:
    """Manage a philosophical debate and handle state transitions."""

    def __init__(self, agent1: Agent, agent2: Agent):
        self.agent1 = agent1
        self.agent2 = agent2
        self.log: List[str] = []

    def run_round(self) -> List[str]:
        """Run a single debate round and update agent states."""
        lines = []
        lines.append(f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}")
        lines.append(f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}")

        # escalate emotions to trigger potential transitions
        self.agent1.update_emotion(self.agent1.emotion + 0.6)
        self.agent2.update_emotion(self.agent2.emotion + 0.6)

        lines.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")
        lines.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")

        self.log.extend(lines)
        return lines
