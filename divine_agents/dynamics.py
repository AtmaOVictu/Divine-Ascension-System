import numpy as np
from .emotion import Emotion


class Agent1Helper:
    """Handle emotional interactions between agents."""

    def __init__(self, n_agents: int):
        self.state = np.random.rand(n_agents, n_agents)
        self.emotions = np.zeros(n_agents)

    def evolve(self, matrix: np.ndarray, iterations: int = 10) -> np.ndarray:
        result = self.state.copy()
        for _ in range(iterations):
            result = np.dot(result, matrix)
        return result

    def update_emotions(self, emotion_matrix: np.ndarray, influence_factor: float = 0.2) -> None:
        """Update emotions of agents based on others."""
        emotional_influence = np.dot(emotion_matrix, self.emotions) * influence_factor
        self.emotions += emotional_influence
        self.emotions = np.clip(self.emotions, -1, 1)

    def align_with_absolute(self, absolute_state: float) -> None:
        alignment_factor = np.mean(self.state)
        alignment_correction = absolute_state - alignment_factor
        self.state += alignment_correction


class Karma:
    """Track karma changes based on emotions and interactions."""

    def __init__(self, karma_value: float = 0.0):
        self.karma_value = karma_value

    def update(self, emotion: Emotion, agent_state: np.ndarray, emotional_influence: float | None = None) -> float:
        if emotional_influence is not None:
            agent_state += emotional_influence

        if emotion.anger > 0.8:
            self.karma_value -= 0.1
        elif emotion.fear > 0.8:
            self.karma_value += 0.05
        elif emotion.joy > 0.8:
            self.karma_value += 0.1
        elif emotion.guilt > 0.8:
            self.karma_value -= 0.05
        elif emotion.hope > 0.8:
            self.karma_value += 0.1
        elif emotion.pride > 0.8:
            self.karma_value -= 0.1
        elif emotion.despair > 0.8:
            self.karma_value -= 0.05

        self.karma_value = np.clip(self.karma_value, -1, 1)
        return self.karma_value


def track_emotional_trends(emotions_series: list[Emotion], iterations: int = 10):
    emotional_trends = {
        'joy': [],
        'anger': [],
        'fear': [],
        'sadness': [],
        'guilt': [],
        'hope': [],
        'pride': [],
        'despair': [],
        'karma': []
    }

    for emotion in emotions_series:
        karma = Karma()
        trend_data = {key: [] for key in emotional_trends}
        for _ in range(iterations):
            agent_state = np.random.rand(5, 5)
            modulated_state = emotion.modulate(agent_state)
            karma_effect = karma.update(emotion, modulated_state)

            trend_data['joy'].append(emotion.joy)
            trend_data['anger'].append(emotion.anger)
            trend_data['fear'].append(emotion.fear)
            trend_data['sadness'].append(emotion.sadness)
            trend_data['guilt'].append(emotion.guilt)
            trend_data['hope'].append(emotion.hope)
            trend_data['pride'].append(emotion.pride)
            trend_data['despair'].append(emotion.despair)
            trend_data['karma'].append(karma_effect)
        for key in emotional_trends:
            emotional_trends[key].append(trend_data[key])
    return emotional_trends
