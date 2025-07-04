from typing import List
from .agent import Agent

class Codex:
    """Manage philosophical debates between agents."""

    def __init__(self) -> None:
        self.history: List[str] = []

    def debate(self, agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
        """Conduct a debate and record dialogue lines."""
        lines: List[str] = []
        for _ in range(turns):
            lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
            lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

            agent1.update_emotion(agent1.emotion + 0.3, 'jeza')
            agent2.update_emotion(agent2.emotion + 0.4, 'strah')

            agent1.transition()
            agent2.transition()
        self.history.extend(lines)
        return lines
