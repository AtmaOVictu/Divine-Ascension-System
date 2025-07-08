from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Sequence

import random


def _clip(value: float, min_value: float, max_value: float) -> float:
    return max(min_value, min(value, max_value))


def _matrix_multiply(a: Sequence[Sequence[float]], b: Sequence[Sequence[float]]) -> List[List[float]]:
    result = [[0.0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i, row in enumerate(a):
        for j in range(len(b[0])):
            total = 0.0
            for k in range(len(b)):
                total += row[k] * b[k][j]
            result[i][j] = total
    return result


def _matrix_vector_multiply(matrix: Sequence[Sequence[float]], vector: Sequence[float]) -> List[float]:
    result = []
    for row in matrix:
        total = 0.0
        for val, v in zip(row, vector):
            total += val * v
        result.append(total)
    return result


@dataclass
class Emotion:
    """Represent various emotional intensities for an agent."""

    joy: float = 0.0
    anger: float = 0.0
    fear: float = 0.0
    sadness: float = 0.0
    guilt: float = 0.0
    hope: float = 0.0
    pride: float = 0.0
    despair: float = 0.0
    regret: float = 0.0
    compassion: float = 0.0
    envy: float = 0.0
    trust: float = 0.0

    def transition(self) -> None:
        """Recover from negative emotions towards positive states."""
        if self.despair > 0.8:
            self.hope = min(1.0, self.hope + 0.4)
            self.despair = max(0.0, self.despair - 0.2)
        elif self.regret > 0.8:
            self.hope = min(1.0, self.hope + 0.2)
            self.regret = max(0.0, self.regret - 0.2)
        elif self.sadness > 0.8:
            self.compassion = min(1.0, self.compassion + 0.3)
            self.sadness = max(0.0, self.sadness - 0.2)


class Karma:
    """Track karma accumulation for an agent."""

    def __init__(self, karma_value: float = 0.0) -> None:
        self.karma_value = karma_value
        self.karma_history: List[float] = []

    def update(
        self,
        emotion: Emotion,
        agent_state: Sequence[Sequence[float]] | None,
        emotional_influence: Optional[Sequence[float]] = None,
    ) -> float:
        if emotional_influence is not None and agent_state is not None:
            # incorporate influence by simple summation on the first row
            agent_state = [
                [val + emotional_influence[i] for i, val in enumerate(row)]
                for row in agent_state
            ]

        if emotion.anger > 0.8:
            self.karma_value -= 0.1
        elif emotion.fear > 0.8:
            self.karma_value += 0.05
        elif emotion.joy > 0.8:
            self.karma_value += 0.1
        elif emotion.regret > 0.8:
            self.karma_value -= 0.15
        elif emotion.compassion > 0.8:
            self.karma_value += 0.2

        self.karma_value = float(_clip(self.karma_value, -1, 1))
        self.karma_history.append(self.karma_value)
        return self.karma_value

    def track_karma_over_time(self) -> List[float]:
        return self.karma_history


class AgentGroup:
    """Handle emotional contagion and state evolution among agents."""

    def __init__(self, n_agents: int) -> None:
        self.state = [[random.random() for _ in range(n_agents)] for _ in range(n_agents)]
        self.emotions = [0.0 for _ in range(n_agents)]

    def evolve(self, matrix: Sequence[Sequence[float]], iterations: int = 10) -> List[List[float]]:
        result = [row[:] for row in self.state]
        for _ in range(iterations):
            result = _matrix_multiply(result, matrix)
        return result

    def update_emotions(
        self, influence_matrix: Sequence[Sequence[float]], influence_factor: float = 0.2
    ) -> None:
        emotional_influence = _matrix_vector_multiply(influence_matrix, self.emotions)
        emotional_influence = [val * influence_factor for val in emotional_influence]
        self.emotions = [_clip(e + i, -1, 1) for e, i in zip(self.emotions, emotional_influence)]

    def align_with_absolute(self, absolute_state: float) -> None:
        flat = [val for row in self.state for val in row]
        alignment_factor = sum(flat) / len(flat)
        alignment_correction = absolute_state - alignment_factor
        self.state = [[val + alignment_correction for val in row] for row in self.state]
