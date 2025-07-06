from typing import List

from .agent import Agent


class DebateSimulator:
    """Simulate an ontological debate between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent, rounds: int = 3):
        self.agent1 = agent1
        self.agent2 = agent2
        self.rounds = rounds

    def _exchange(self) -> List[str]:
        """One exchange of dialogue based on current states."""
        lines = [
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}",
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}"
        ]
        return lines

    def run(self) -> List[str]:
        """Execute the debate for a given number of rounds."""
        conversation: List[str] = []
        for _ in range(self.rounds):
            conversation.extend(self._exchange())
            # Increase emotions which also raises tension
            self.agent1.update_emotion(self.agent1.emotion + 0.3)
            self.agent2.update_emotion(self.agent2.emotion + 0.3)
            conversation.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")
            conversation.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")
        return conversation
