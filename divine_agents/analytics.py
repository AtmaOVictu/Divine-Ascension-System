from typing import Dict, List
import random
from .emotions import Emotion
from .karma import Karma


def track_emotional_trends(emotions_series: List[Emotion], iterations: int = 10) -> Dict[str, List[List[float]]]:
    """Track emotional states and karma over multiple iterations."""
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
            agent_state = [[random.random() for _ in range(5)] for _ in range(5)]
            modulated_state = emotion.modulate(agent_state)
            karma_value = karma.update(emotion, modulated_state)

            trend_data['joy'].append(emotion.joy)
            trend_data['anger'].append(emotion.anger)
            trend_data['fear'].append(emotion.fear)
            trend_data['sadness'].append(emotion.sadness)
            trend_data['guilt'].append(emotion.guilt)
            trend_data['hope'].append(emotion.hope)
            trend_data['pride'].append(emotion.pride)
            trend_data['despair'].append(emotion.despair)
            trend_data['karma'].append(karma_value)
        for key in emotional_trends:
            emotional_trends[key].append(trend_data[key])
    return emotional_trends
