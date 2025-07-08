import numpy as np

class Agent1Helper:
    """Utility class for agent state evolution and emotional contagion."""

    def __init__(self, n_agents: int):
        self.state = np.random.rand(n_agents, n_agents)
        self.emotions = np.zeros(n_agents)

    def evolve(self, matrix, iterations: int = 10):
        result = [row.copy() for row in self.state]
        for _ in range(iterations):
            result = np.dot(result, matrix)
        return result

    def update_emotions(self, influence_matrix, influence_factor: float = 0.2) -> None:
        emotional_influence = [
            sum(influence_matrix[i][j] * self.emotions[j] for j in range(len(self.emotions))) * influence_factor
            for i in range(len(influence_matrix))
        ]
        self.emotions = [e + inf for e, inf in zip(self.emotions, emotional_influence)]
        self.emotions = np.clip(self.emotions, -1, 1)

    def align_with_absolute(self, absolute_state: float) -> None:
        alignment_factor = np.mean(self.state)
        alignment_correction = absolute_state - alignment_factor
        self.state = [
            [cell + alignment_correction for cell in row] for row in self.state
        ]
