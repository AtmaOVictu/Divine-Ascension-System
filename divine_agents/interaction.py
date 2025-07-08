from __future__ import annotations

from typing import List


def _identity(size: int) -> List[List[float]]:
    return [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]

from .agent import Agent


class EmotionalNetwork:
    """Manage emotional influence between agents."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.matrix = _identity(len(agents))

    def set_influence_matrix(self, matrix: List[List[float]]) -> None:
        if len(matrix) != len(self.agents) or any(len(row) != len(self.agents) for row in matrix):
            raise ValueError("Matrix size must match number of agents")
        self.matrix = matrix

    def propagate(self, influence_factor: float = 0.2) -> None:
        emotions = [a.emotion for a in self.agents]
        influence = []
        for row in self.matrix:
            value = sum(r * e for r, e in zip(row, emotions)) * influence_factor
            influence.append(value)
        for agent, inf in zip(self.agents, influence):
            agent.update_emotion(agent.emotion + inf)

