"""Tools for managing dialogues between ontological agents."""

from typing import List

from .agent import Agent


class Conversation:
    """Facilitate philosophical debate between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def step(self, emotion1: float, emotion2: float) -> None:
        """Execute a single exchange and handle state transitions."""
        self.agent1.update_emotion(emotion1)
        line1 = f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}"
        self.history.append(line1)
        self.agent1.transition()

        self.agent2.update_emotion(emotion2)
        line2 = f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"
        self.history.append(line2)
        self.agent2.transition()

    def run(self, rounds: int, emotions1: List[float], emotions2: List[float]) -> List[str]:
        """Run multiple rounds of conversation."""
        for i in range(rounds):
            self.step(emotions1[i], emotions2[i])
        return self.history
