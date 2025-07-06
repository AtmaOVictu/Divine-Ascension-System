from typing import List
from .agent import Agent


class PhilosophicalDialogue:
    """Manage a dialogue between two agents influenced by emotions."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def start(self) -> List[str]:
        lines: List[str] = []
        lines.append(
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"
        )

        self.agent1.update_emotion(0.8)
        self.agent2.update_emotion(0.6)

        lines.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")
        lines.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")

        lines.append(
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"
        )

        self.history.extend(lines)
        return lines
