from __future__ import annotations

import random

from .emotion import Emotion
from .karma import Karma


def track_emotional_trends(emotions_series: list[Emotion], iterations: int = 10):
    """Track emotional and karma trends for a list of emotions."""
    trends = {
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
        local = {k: [] for k in trends}
        for _ in range(iterations):
            agent_state = [[random.random() for _ in range(3)] for _ in range(3)]
            modulated = emotion.modulate(agent_state)
            karma_effect = karma.update(emotion, modulated)
            local['joy'].append(emotion.joy)
            local['anger'].append(emotion.anger)
            local['fear'].append(emotion.fear)
            local['sadness'].append(emotion.sadness)
            local['guilt'].append(emotion.guilt)
            local['hope'].append(emotion.hope)
            local['pride'].append(emotion.pride)
            local['despair'].append(emotion.despair)
            local['karma'].append(karma_effect)
        for k in trends:
            trends[k].append(local[k])
    return trends


def plot_trends(trends):
    """Return a textual representation of the first trend for quick inspection."""
    lines = [
        f"Joy: {trends['joy'][0]}",
        f"Anger: {trends['anger'][0]}",
        f"Karma: {trends['karma'][0]}",
    ]
    return "\n".join(lines)
