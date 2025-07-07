from __future__ import annotations
import random
from typing import List
from .voice_agent import VoiceAgent


class Cluster:
    """Cluster of agents that synchronize transitions."""

    def __init__(self, agents: List[VoiceAgent]):
        self.agents = agents
        self.history: List[str] = []

    def synchronize(self) -> None:
        """Synchronize emotional updates and transitions for all agents."""
        for agent in self.agents:
            # Random emotional fluctuations
            agent.update_emotion(agent.mood, random.uniform(0, 1))
            agent.update_tension(random.uniform(0, 1))
            new_state = agent.transition()
            self.history.append(f"{agent.name} transitioned to {new_state}")

    def display_dialogue(self) -> List[str]:
        """Return a dialogue reflecting each agent's current state."""
        lines: List[str] = []
        for agent in self.agents:
            lines.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
        return lines
