"""Cluster module to manage groups of agents and their interactions."""
from __future__ import annotations

from typing import Iterable, List, Optional
import random

from .agent import Agent


class Cluster:
    """Group of agents that evolve together."""

    def __init__(self, agents: Iterable[Agent]):
        self.agents: List[Agent] = list(agents)

    def synchronize(self, emotions: Optional[Iterable[float]] = None, tensions: Optional[Iterable[float]] = None) -> List[str]:
        """Synchronize all agents by applying emotions and tensions then transitioning.

        Parameters
        ----------
        emotions:
            Optional iterable of emotion values to assign to agents.
        tensions:
            Optional iterable of tension values to assign to agents.
        """
        lines = []
        emotions = list(emotions) if emotions is not None else [random.uniform(0, 1) for _ in self.agents]
        tensions = list(tensions) if tensions is not None else [random.uniform(0, 1) for _ in self.agents]
        for idx, agent in enumerate(self.agents):
            agent.update_emotion(emotions[idx])
            agent.update_tension(tensions[idx])
            state = agent.transition()
            lines.append(f"{agent.name} ({state}): {agent.respond('Kaj je resnica?')}")
        return lines
