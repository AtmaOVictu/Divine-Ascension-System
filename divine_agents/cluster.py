from __future__ import annotations

import random
from typing import List

from .voice_agent import VoiceAgent


class Cluster:
    """Cluster of agents transitioning through shared emotional and philosophical states."""

    def __init__(self, agents: List[VoiceAgent]):
        self.agents = agents
        self.history: List[str] = []

    def synchronize(self) -> None:
        """Synchronize transitions across all agents based on their emotional states."""
        for agent in self.agents:
            # Apply mood-based emotional changes
            agent.update_emotion(agent.mood, random.uniform(0, 1))
            transition_result = agent.transition()
            self.history.append(f"{agent.name} transitioned to {transition_result}")

    def display_dialogue(self) -> List[str]:
        """Simulate a dialogue between agents, reflecting emotional tones and transitions."""
        dialogue: List[str] = []
        for agent in self.agents:
            dialogue.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
        return dialogue
