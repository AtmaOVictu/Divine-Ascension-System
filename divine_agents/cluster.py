import random
from typing import List
from .agent import Agent


class Cluster:
    """Cluster of agents transitioning through shared emotional states."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.history: List[str] = []

    def synchronize(self) -> None:
        """Synchronize transitions across all agents."""
        for agent in self.agents:
            agent.update_emotion(agent.mood, random.uniform(0, 1))
            agent.update_tension(random.uniform(0, 1))
            state = agent.transition()
            self.history.append(f"{agent.name} transitioned to {state}")

    def display_dialogue(self) -> List[str]:
        """Create a dialogue snapshot for the cluster."""
        dialogue: List[str] = []
        for agent in self.agents:
            dialogue.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
        return dialogue

