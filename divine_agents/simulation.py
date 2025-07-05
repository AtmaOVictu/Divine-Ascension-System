"""Simple simulation utilities for biological and social transitions."""

from typing import Iterable, List

from .agent import Agent
from .transitions import biological_transition, social_transition


def run_agent_simulation(
    agents: Iterable[Agent],
    k_bio: float,
    c_bio: float,
    k_soc: float,
    c_soc: float,
    steps: int = 100,
) -> List[List[float]]:
    """Evolve agents using logistic transitions and return state histories."""
    bio_history: List[List[float]] = []
    soc_history: List[List[float]] = []

    for _ in range(steps):
        bio_step = []
        soc_step = []
        for agent in agents:
            agent.state_bio = biological_transition(agent.emotion, k_bio, c_bio)
            agent.state_soc = social_transition(agent.tension, k_soc, c_soc)
            bio_step.append(agent.state_bio)
            soc_step.append(agent.state_soc)
        bio_history.append(bio_step)
        soc_history.append(soc_step)

    return bio_history, soc_history
