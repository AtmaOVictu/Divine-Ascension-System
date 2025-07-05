"""Simulation utilities that drive agents through philosophical states."""

from typing import Iterable, List

from .agent import Agent
from .math_models import logistic_function, logarithmic_function


def simulate_agent_progression(
    agent: Agent,
    time_steps: Iterable[float],
    k_logistic: float = 1.5,
    c_logistic: float = 0.5,
    k_log: float = 1.0,
    c_log: float = 1.0,
) -> List[str]:
    """Simulate emotional and tension growth using logistic and logarithmic models.

    Returns a history of agent states after each step.
    """

    states = []
    for t in time_steps:
        emotion = logistic_function(t, k_logistic, c_logistic)
        tension = logarithmic_function(t, k_log, c_log)
        agent.update_emotion(emotion)
        agent.update_tension(tension)
        states.append(agent.transition())
    return states
