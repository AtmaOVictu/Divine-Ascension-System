"""Utilities for boxing ontological agents as a modular library."""
from __future__ import annotations

import random
from typing import List


# ---------- Matrix helpers ----------

def initialize_agents(n_agents: int) -> List[List[float]]:
    """Return a square matrix representing initial agent states."""
    return [[random.random() for _ in range(n_agents)] for _ in range(n_agents)]


def _matmul(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Multiply two square matrices."""
    n = len(a)
    result = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def recursive_evolution(agent_matrix: List[List[float]], iterations: int = 10) -> List[List[float]]:
    """Evolve agent matrix via repeated multiplication."""
    result = [row[:] for row in agent_matrix]
    for _ in range(iterations):
        result = _matmul(result, agent_matrix)
    return result


def transition_function(agent_state: List[float], transition_matrix: List[List[float]]) -> List[float]:
    """Apply a transition matrix to an agent state vector."""
    size = len(transition_matrix)
    result = [0.0 for _ in range(size)]
    for i in range(size):
        for j, val in enumerate(agent_state):
            result[i] += val * transition_matrix[j][i]
    return result


class OntoscienceBox:
    """Boxed representation of ontological agents and their evolution."""

    def __init__(self, n_agents: int, iterations: int = 10) -> None:
        self.agent_matrix = initialize_agents(n_agents)
        self.iterations = iterations

    def evolve_agents(self) -> List[List[float]]:
        """Simulate recursive evolution of agent states."""
        self.agent_matrix = recursive_evolution(self.agent_matrix, self.iterations)
        return self.agent_matrix

    def apply_transition(self, transition_matrix: List[List[float]]) -> List[List[float]]:
        """Apply a transition function to the internal matrix."""
        new_matrix = []
        for row in self.agent_matrix:
            new_matrix.append(transition_function(row, transition_matrix))
        self.agent_matrix = new_matrix
        return self.agent_matrix

    def get_agent_states(self) -> List[List[float]]:
        """Return the current agent matrix."""
        return [row[:] for row in self.agent_matrix]
