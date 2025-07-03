"""Simple interpolation utilities for agent differences without external deps."""
from typing import Iterable, List, Tuple
from .agent import Agent


def linear_interpolate(start: float, end: float, steps: int) -> List[float]:
    """Return a list of `steps` linearly interpolated values between start and end."""
    if steps < 2:
        return [start]
    step = (end - start) / (steps - 1)
    return [start + i * step for i in range(steps)]


def quadratic_interpolate(start: float, end: float, steps: int) -> List[float]:
    """Quadratic interpolation using simple square progression."""
    if steps < 2:
        return [start]
    values = []
    for i in range(steps):
        t = i / (steps - 1)
        # simple parabola going through (0,start) and (1,end)
        values.append((1 - t) ** 2 * start + t ** 2 * end)
    return values


def interpolate_differences(agent1: Agent, agent2: Agent, times: Iterable[float]) -> Tuple[List[float], List[float]]:
    """Calculate emotion and tension difference interpolations between two agents."""
    t = list(times)
    steps = len(t)
    emotion_start = agent1.emotion - agent2.emotion
    tension_start = agent1.tension - agent2.tension
    emotion_interp = linear_interpolate(emotion_start, 0.0, steps)
    tension_interp = quadratic_interpolate(tension_start, 0.0, steps)
    return emotion_interp, tension_interp
