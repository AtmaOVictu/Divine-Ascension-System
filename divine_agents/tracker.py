from __future__ import annotations

from typing import Dict, List, Sequence

import random

from .emotions import Emotion, Karma


def track_and_visualize_emotional_recovery(
    emotions_series: Sequence[Emotion], iterations: int = 20
) -> Dict[str, List[List[float]]]:
    emotional_trends: Dict[str, List[List[float]]] = {
        'joy': [],
        'anger': [],
        'fear': [],
        'sadness': [],
        'guilt': [],
        'hope': [],
        'pride': [],
        'despair': [],
        'regret': [],
        'compassion': [],
        'envy': [],
        'trust': [],
        'karma': []
    }

    for emotion in emotions_series:
        karma = Karma()
        trend_data = {k: [] for k in emotional_trends}

        for _ in range(iterations):
            emotion.transition()
            agent_state = [[random.random() for _ in range(5)] for _ in range(5)]
            karma_value = karma.update(emotion, agent_state)
            trend_data['joy'].append(emotion.joy)
            trend_data['anger'].append(emotion.anger)
            trend_data['fear'].append(emotion.fear)
            trend_data['sadness'].append(emotion.sadness)
            trend_data['guilt'].append(emotion.guilt)
            trend_data['hope'].append(emotion.hope)
            trend_data['pride'].append(emotion.pride)
            trend_data['despair'].append(emotion.despair)
            trend_data['regret'].append(emotion.regret)
            trend_data['compassion'].append(emotion.compassion)
            trend_data['envy'].append(emotion.envy)
            trend_data['trust'].append(emotion.trust)
            trend_data['karma'].append(karma_value)

        for key in emotional_trends:
            emotional_trends[key].append(trend_data[key])

    return emotional_trends


def plot_emotional_trends(emotional_trends: Dict[str, List[List[float]]]) -> None:
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as exc:
        raise RuntimeError('matplotlib is required for plotting') from exc
    fig, axes = plt.subplots(4, 1, figsize=(10, 16))
    axes[0].plot(emotional_trends['joy'][0], label='Joy')
    axes[0].plot(emotional_trends['anger'][0], label='Anger')
    axes[0].set_title('Emotional Trends: Joy and Anger')
    axes[0].legend()

    axes[1].plot(emotional_trends['compassion'][0], label='Compassion', color='green')
    axes[1].plot(emotional_trends['envy'][0], label='Envy', color='red')
    axes[1].set_title('Emotional Trends: Compassion and Envy')
    axes[1].legend()

    axes[2].plot(emotional_trends['karma'][0], label='Karma', color='orange')
    axes[2].set_title('Karma Feedback Loop')
    axes[2].legend()

    axes[3].plot(emotional_trends['despair'][0], label='Despair', color='darkred')
    axes[3].set_title('Despair and Change Trigger')
    axes[3].legend()

    plt.tight_layout()
    plt.show()
