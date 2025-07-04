# -*- coding: utf-8 -*-
"""Module for managing dynamic interactions between agents."""

from typing import List
from .agent import Agent


class InteractionManager:
    """Simulate dialogues and manage state transitions based on emotions."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2

    def exchange(self, emotion1: float, emotion2: float) -> List[str]:
        """Perform one exchange between agents with given emotional inputs."""
        lines = []
        # Initial responses reflecting current ontological states
        lines.append(f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}")
        lines.append(f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}")

        # Update emotions which may affect tension and trigger transitions
        self.agent1.update_emotion(emotion1)
        lines.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")

        self.agent2.update_emotion(emotion2)
        lines.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")

        # Final responses after potential transitions
        lines.append(f"{self.agent1.name}: {self.agent1.respond('Kaj je resnica?')}")
        lines.append(f"{self.agent2.name}: {self.agent2.respond('Kaj je resnica?')}")
        return lines

    def simulate(self, steps: List[tuple]) -> List[str]:
        """Run multiple exchanges given a list of emotion pairs."""
        dialogue: List[str] = []
        for emotion1, emotion2 in steps:
            dialogue.extend(self.exchange(emotion1, emotion2))
        return dialogue
