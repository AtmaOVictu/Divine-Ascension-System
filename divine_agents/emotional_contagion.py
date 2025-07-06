# -*- coding: utf-8 -*-
"""Utility for spreading emotional states between agents."""
from __future__ import annotations

from typing import List

from .agent import Agent


class EmotionalContagion:
    """Simple model to propagate emotions among registered agents."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Register an agent to the contagion system."""
        self.agents.append(agent)

    def spread_emotion(self, agent_index: int, influence: float) -> None:
        """Spread the selected agent's emotion to all other agents."""
        source = self.agents[agent_index]
        for idx, other in enumerate(self.agents):
            if idx == agent_index:
                continue
            other.update_emotion(source.emotion + influence)
