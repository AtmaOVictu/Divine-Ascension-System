"""Utility functions for computing differences and interpolating agent data."""

from typing import List, Tuple
from .agent import Agent


def linspace(start: float, stop: float, num: int) -> List[float]:
    """Return a list of evenly spaced numbers over a specified interval."""
    if num < 2:
        return [start]
    step = (stop - start) / (num - 1)
    return [start + step * i for i in range(num)]


def linear_interpolate(x: List[float], xp: List[float], fp: List[float]) -> List[float]:
    """Perform simple linear interpolation."""
    if len(xp) != len(fp) or len(xp) < 2:
        raise ValueError("Invalid input data for interpolation")

    result: List[float] = []
    for value in x:
        if value <= xp[0]:
            result.append(fp[0])
            continue
        if value >= xp[-1]:
            result.append(fp[-1])
            continue
        # find interval
        for i in range(len(xp) - 1):
            if xp[i] <= value <= xp[i + 1]:
                slope = (fp[i + 1] - fp[i]) / (xp[i + 1] - xp[i])
                result.append(fp[i] + slope * (value - xp[i]))
                break
    return result


def interpolate_differences(agent1: Agent, agent2: Agent, steps: int = 50) -> Tuple[List[float], List[float], List[float]]:
    """Interpolate emotion and tension differences between two agents."""
    length = min(len(agent1.emotion_history), len(agent2.emotion_history))
    if length < 2:
        raise ValueError("Agents must have at least two history points for interpolation")

    time_points = list(range(length))
    emo_diff = [a - b for a, b in zip(agent1.emotion_history[:length], agent2.emotion_history[:length])]
    tens_diff = [a - b for a, b in zip(agent1.tension_history[:length], agent2.tension_history[:length])]

    interp_time = linspace(time_points[0], time_points[-1], steps)
    emo_interp = linear_interpolate(interp_time, time_points, emo_diff)
    tens_interp = linear_interpolate(interp_time, time_points, tens_diff)

    return interp_time, emo_interp, tens_interp
