from typing import List
from .agent import Agent


class DialogueManager:
    """Manage philosophical dialogue between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        """Initialize the manager with two participating agents."""
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def step(self, emotion1: float, emotion2: float) -> List[str]:
        """Run a single exchange and update agent states."""
        lines = []
        lines.append(f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}")
        lines.append(f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}")

        self.agent1.update_emotion(emotion1)
        lines.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")

        self.agent2.update_emotion(emotion2)
        lines.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")

        self.history.extend(lines)
        return lines

    def run(self, emotions1: List[float], emotions2: List[float]) -> List[str]:
        """Run multiple exchanges with provided emotion sequences."""
        for e1, e2 in zip(emotions1, emotions2):
            self.step(e1, e2)
        return self.history
