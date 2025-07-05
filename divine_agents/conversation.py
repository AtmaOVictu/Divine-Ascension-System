from typing import List

from .agent import Agent


class Conversation:
    """Simulate a philosophical conversation between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def step(self, question: str) -> List[str]:
        """Execute a single step of the conversation."""
        lines = [
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond(question)}",
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond(question)}",
        ]

        # Increase emotions which also affects tension
        self.agent1.update_emotion(0.4)
        lines.append(f"{self.agent1.name} transitions to: {self.agent1.transition()}")
        self.agent2.update_emotion(0.6)
        lines.append(f"{self.agent2.name} transitions to: {self.agent2.transition()}")

        self.history.extend(lines)
        return lines

    def run(self, question: str, steps: int = 3) -> List[str]:
        """Run several conversation steps."""
        dialogue: List[str] = []
        for _ in range(steps):
            dialogue.extend(self.step(question))
        return dialogue
