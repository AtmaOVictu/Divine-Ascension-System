from __future__ import annotations

from typing import List

from .voice_agent import VoiceAgent


class Cluster:
    """Group of agents transitioning through shared emotional states."""

    def __init__(self, agents: List[VoiceAgent]):
        self.agents = agents
        self.history: List[str] = []

    def synchronize(self) -> None:
        """Synchronize transitions based on each agent's emotion and tension."""
        for agent in self.agents:
            agent.transition()
            self.history.append(f"{agent.name} transitioned to {agent.state}")

    def display_dialogue(self) -> List[str]:
        """Return a dialogue snapshot for all agents."""
        return [f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}" for agent in self.agents]
