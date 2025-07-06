"""Simulation of multiple agents' energy and tension over time."""

from __future__ import annotations

import random
from typing import List, Tuple

from .agent import Agent


class Ecosystem:
    """Manage a collection of agents and update them over time."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def step(self) -> None:
        """Advance simulation one step by applying random capacitors."""
        for agent in self.agents:
            cap = random.choice([0.5, 1.0, 1.5])
            agent.apply_capacitor(cap)
            agent.transition()

    def run(self, steps: int) -> Tuple[List[List[float]], List[List[float]]]:
        """Simulate agents for a number of steps.

        Returns arrays of energy and tension for each agent over time.
        """
        energy_hist = [[0.0 for _ in self.agents] for _ in range(steps)]
        tension_hist = [[0.0 for _ in self.agents] for _ in range(steps)]

        for t in range(steps):
            self.step()
            for idx, agent in enumerate(self.agents):
                energy_hist[t][idx] = agent.energy
                tension_hist[t][idx] = agent.tension
        return energy_hist, tension_hist


def create_default_ecosystem() -> Ecosystem:
    """Create an ecosystem with five default agents."""
    agents = [
        Agent("A", energy=50, tension=20),
        Agent("B", energy=60, tension=15),
        Agent("C", energy=55, tension=25),
        Agent("D", energy=45, tension=30),
        Agent("E", energy=40, tension=35),
    ]
    return Ecosystem(agents)
