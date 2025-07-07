from __future__ import annotations

from typing import List
from uuid import uuid4

from .agent import Agent


class Conversation:
    """Manage a philosophical conversation between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.id = uuid4()

    def _exchange(self, speaker: Agent, listener: Agent) -> str:
        """Generate dialogue line and update states based on emotions."""
        response = speaker.respond("Kaj je resnica?")
        line = f"{speaker.name} ({speaker.state}): {response}"
        # Increase emotion slightly to simulate tension build-up
        speaker.update_emotion(min(speaker.emotion + 0.3, 1.0))
        speaker.transition()
        return line

    def run(self, turns: int = 2) -> List[str]:
        """Run the conversation for a number of turns."""
        lines: List[str] = []
        for _ in range(turns):
            lines.append(self._exchange(self.agent1, self.agent2))
            lines.append(self._exchange(self.agent2, self.agent1))
        return lines
