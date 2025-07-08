from __future__ import annotations

from typing import List, Dict

import matplotlib.pyplot as plt
import random

from .karma import Karma
from .agent import Agent


def track_emotional_trends(agents: List[Agent], iterations: int = 10) -> Dict[str, List[List[float]]]:
    """Track emotional and karma trends for each agent."""
    emotional_trends = {k: [] for k in ["emotion", "karma"]}

    for agent in agents:
        karma = Karma()
        emotion_series = []
        karma_series = []
        for _ in range(iterations):
            # simple random modulation to illustrate changes
            delta = random.uniform(-0.1, 0.1)
            new_emotion = max(min(agent.emotion + delta, 1.0), -1.0)
            agent.update_emotion(new_emotion)
            class _E:
                pass

            e = _E()
            e.joy = max(agent.emotion, 0.0)
            karma_value = karma.update(e, agent.tension)
            emotion_series.append(agent.emotion)
            karma_series.append(karma_value)
        emotional_trends["emotion"].append(emotion_series)
        emotional_trends["karma"].append(karma_series)
    return emotional_trends


def plot_trends(trends: Dict[str, List[List[float]]]) -> None:
    """Plot emotion and karma trends for the first agent."""
    fig, ax = plt.subplots(2, 1, figsize=(8, 6))
    ax[0].plot(trends["emotion"][0], label="Emotion")
    ax[0].legend()
    ax[1].plot(trends["karma"][0], label="Karma", color="orange")
    ax[1].legend()
    plt.tight_layout()
    plt.show()
