import random
from typing import List

class AgentNetwork:
    """Manage emotional interactions between multiple agents."""

    def __init__(self, n_agents: int):
        self.state = [[random.random() for _ in range(n_agents)] for _ in range(n_agents)]
        self.emotions = [0.0 for _ in range(n_agents)]

    def evolve(self, matrix: List[List[float]], iterations: int = 10) -> List[List[float]]:
        """Recursively evolve internal state through matrix multiplication."""
        result = [row[:] for row in self.state]
        for _ in range(iterations):
            result = _matrix_multiply(result, matrix)
        return result

    def update_emotions(self, emotion_matrix: List[List[float]], influence_factor: float = 0.2) -> None:
        """Propagate emotional influence across agents."""
        influence = _matrix_vector_multiply(emotion_matrix, self.emotions)
        self.emotions = [max(-1.0, min(1.0, e + inf * influence_factor)) for e, inf in zip(self.emotions, influence)]

    def align_with_absolute(self, absolute_state: float) -> None:
        """Align internal state toward an absolute value."""
        mean_state = sum(sum(row) for row in self.state) / (len(self.state) * len(self.state))
        correction = absolute_state - mean_state
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                self.state[i][j] += correction


def _matrix_multiply(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    result = [[0.0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def _matrix_vector_multiply(matrix: List[List[float]], vector: List[float]) -> List[float]:
    result = [0.0 for _ in range(len(matrix))]
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            result[i] += val * vector[j]
    return result
