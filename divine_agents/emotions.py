"""Emotion and Karma management for agents."""
from __future__ import annotations
import random


class Emotion:
    """Container for multiple emotional states."""

    def __init__(self, joy: float = 0.0, anger: float = 0.0, fear: float = 0.0,
                 sadness: float = 0.0, guilt: float = 0.0, hope: float = 0.0,
                 pride: float = 0.0, despair: float = 0.0) -> None:
        self.joy = joy
        self.anger = anger
        self.fear = fear
        self.sadness = sadness
        self.guilt = guilt
        self.hope = hope
        self.pride = pride
        self.despair = despair

    def modulate(self, agent_state: float) -> float:
        """Return agent state influenced by current emotions."""
        emotional_value = (
            (self.joy * 0.3)
            + (self.anger * 0.2)
            - (self.fear * 0.1)
            - (self.sadness * 0.15)
            - (self.guilt * 0.2)
            + (self.hope * 0.25)
            + (self.pride * 0.1)
            - (self.despair * 0.3)
        )
        return agent_state * (1 + emotional_value)


class Karma:
    """Accumulates positive or negative karma over time."""

    def __init__(self, karma_value: float = 0.0) -> None:
        self.karma_value = karma_value

    def update(self, emotion: Emotion, agent_state: float) -> float:
        """Update karma based on an agent's emotional state."""
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

        self.karma_value = max(-1.0, min(1.0, float(self.karma_value)))
        return self.karma_value


def track_emotional_trends(emotions_series: list[Emotion], iterations: int = 10) -> dict:
    """Track emotion and karma changes over multiple iterations."""
    emotional_trends = {
        'joy': [], 'anger': [], 'fear': [], 'sadness': [], 'guilt': [],
        'hope': [], 'pride': [], 'despair': [], 'karma': []
    }

    for emotion in emotions_series:
        karma = Karma()
        trend_data = {k: [] for k in emotional_trends}
        for _ in range(iterations):
            state = random.random()
            _ = emotion.modulate(state)
            karma_effect = karma.update(emotion, state)
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
