from typing import List
from .agent import Agent

class Conversation:
    """Manage a dialogue between two ontological agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def step(self, emotion1: float, emotion2: float) -> List[str]:
        """Run a single step of the conversation and return both responses."""
        self.agent1.update_emotion(emotion1)
        self.agent2.update_emotion(emotion2)

        self.agent1.transition()
        self.agent2.transition()

        line1 = f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}"
        line2 = f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"

        self.history.extend([line1, line2])
        return [line1, line2]
