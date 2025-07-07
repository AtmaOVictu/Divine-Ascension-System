from __future__ import annotations

import random
from typing import List

from .voice_agent import VoiceAgent


class Cluster:
    """Cluster managing multiple VoiceAgents and their collective transitions."""

    def __init__(self, agents: List[VoiceAgent]):
        self.agents = agents
        self.history: List[str] = []

    def synchronize(self) -> None:
        """Synchronize transitions across all agents using their moods."""
        for agent in self.agents:
            value = random.uniform(0, 1)
            agent.update_emotion(agent.mood, value)
            agent.transition()
            self.history.append(f"{agent.name} transitioned to {agent.state}")

    def display_dialogue(self) -> List[str]:
        """Return a dialogue snippet from all agents."""
        lines = []
        for agent in self.agents:
            lines.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
        return lines
