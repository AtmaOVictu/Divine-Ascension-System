from typing import List, Tuple
from .agent import Agent
import random


def run_simulation(agents: List[Agent], time_steps: int) -> Tuple[List[List[float]], List[List[float]]]:
    """Run a simple energy/tension simulation for the provided agents."""
    energy_hist = [[0.0 for _ in agents] for _ in range(time_steps)]
    tension_hist = [[0.0 for _ in agents] for _ in range(time_steps)]
    for t in range(time_steps):
        for i, agent in enumerate(agents):
            capacitor = random.choice([0.5, 1.0, 1.5])
            agent.apply_influence(capacitor)
            energy_hist[t][i] = agent.energy
            tension_hist[t][i] = agent.tension
    return energy_hist, tension_hist
