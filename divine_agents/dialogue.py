from typing import List

from .agent import Agent


class DialogueManager:
    """Manage philosophical dialogue between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2

    def _exchange(self) -> List[str]:
        """Return lines for a single exchange."""
        return [
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}",
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}",
        ]

    def run_dialogue(self) -> List[str]:
        """Run a short dialogue with emotion induced transitions."""
        lines = []
        lines.extend(self._exchange())

        self.agent1.update_emotion(0.8, "jeza")
        prev1 = self.agent1.state
        self.agent1.transition()
        if self.agent1.state != prev1:
            lines.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.state}")

        self.agent2.update_emotion(0.6, "strah")
        prev2 = self.agent2.state
        self.agent2.transition()
        if self.agent2.state != prev2:
            lines.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.state}")

        lines.extend(
            [f"{self.agent1.name}: {self.agent1.respond('Kaj je resnica?')}",
             f"{self.agent2.name}: {self.agent2.respond('Kaj je resnica?')}"]
        )
        return lines
