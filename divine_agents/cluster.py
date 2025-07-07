import random
from typing import List

from .voice_agent import VoiceAgent


class Cluster:
    """Group of voice agents transitioning through shared states."""

    def __init__(self, agents: List[VoiceAgent]):
        self.agents = agents
        self.history = []

    def synchronize(self) -> None:
        """Synchronize emotional transitions across all agents."""
        for agent in self.agents:
            agent.update_emotion(agent.mood, random.uniform(0, 1))
            agent.update_tension(random.uniform(0, 1))
            new_state = agent.transition()
            self.history.append(f"{agent.name} transitioned to {new_state}")

    def display_dialogue(self) -> List[str]:
        """Return a dialogue reflecting each agent's current state and emotion."""
        dialogue = []
        for agent in self.agents:
            dialogue.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
            dialogue.append(f"{agent.name} transitions to: {agent.state}")
        return dialogue
