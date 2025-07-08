from . import simple_numpy as np

class AgentHelper:
    """Utility to manage emotional contagion between agents."""

    def __init__(self, n_agents: int):
        self.state = np.rand(n_agents, n_agents)
        self.emotions = np.zeros(n_agents)

    def evolve(self, matrix, iterations: int = 10):
        result = [row[:] for row in self.state]
        for _ in range(iterations):
            result = np.dot(result, matrix)
        return result

    def update_emotions(self, influence_matrix, influence_factor: float = 0.2):
        emotional_influence = np.dot(influence_matrix, self.emotions)
        emotional_influence = [val * influence_factor for val in emotional_influence]
        self.emotions = [e + inf for e, inf in zip(self.emotions, emotional_influence)]
        self.emotions = np.clip(self.emotions, -1, 1)
        return self.emotions

    def align_with_absolute(self, absolute_state):
        alignment_factor = np.mean(self.state)
        alignment_correction = absolute_state - alignment_factor
        self.state = [[val + alignment_correction for val in row] for row in self.state]
