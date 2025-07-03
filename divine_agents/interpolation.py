from .agent import Agent


def interpolate_differences(agent1: Agent, agent2: Agent, steps: int = 50):
    """Return interpolated emotion and tension differences over time."""
    if steps < 2:
        raise ValueError("steps must be >= 2")

    time = [i / (steps - 1) for i in range(steps)]
    emotion_start = agent1.emotion - agent2.emotion
    tension_start = agent1.tension - agent2.tension

    emotion_diff = [emotion_start * (1 - t) for t in time]
    tension_diff = [tension_start * (1 - t) for t in time]

    return {
        "time": time,
        "emotion_diff": emotion_diff,
        "tension_diff": tension_diff,
    }

