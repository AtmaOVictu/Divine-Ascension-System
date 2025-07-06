from typing import List
from .agent import Agent


class PhilosophicalDialogue:
    """Manage philosophical exchanges between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def exchange(self, question: str) -> List[str]:
        """Perform a short dialogue sequence and update agent states."""
        lines: List[str] = []

        lines.append(f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond(question)}")
        lines.append(f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond(question)}")
        self.history.extend(lines)

        # Update emotional states after initial exchange
        self.agent1.set_emotional_state("thoughtful", 0.6)
        lines.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")

        self.agent2.set_emotional_state("curious", 0.4)
        lines.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")

        # Second round of answers after possible transitions
        lines.append(f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond(question)}")
        lines.append(f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond(question)}")
        self.history.extend(lines[-2:])

        return lines
