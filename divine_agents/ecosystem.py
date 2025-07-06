import random
from typing import List, Tuple

from .agent import Agent


def simulate_ecosystem(
    agents: List[Agent], steps: int = 10
) -> Tuple[List[List[float]], List[List[float]], List[List[str]]]:
    """Simulate an ecosystem where agents evolve based on capacitors."""
    kapacitatorji = [random.uniform(0.5, 1.5) for _ in agents]
    energy = [random.uniform(0.1, 0.9) for _ in agents]
    tension = [random.uniform(0.2, 1.0) for _ in agents]

    energy_hist = []
    tension_hist = []
    state_hist: List[List[str]] = []

    for _ in range(steps):
        d_energy = [random.gauss(0, 1) * k for k in kapacitatorji]
        d_tension = [random.gauss(0, 1) * k for k in kapacitatorji]

        energy = [min(1.0, max(0.0, e + de)) for e, de in zip(energy, d_energy)]
        tension = [min(1.0, max(0.0, t + dt)) for t, dt in zip(tension, d_tension)]

        energy_hist.append(list(energy))
        tension_hist.append(list(tension))

        step_states = []
        for idx, ag in enumerate(agents):
            ag.update_tension(tension[idx])
            ag.transition()
            step_states.append(ag.state)
        state_hist.append(step_states)

    return energy_hist, tension_hist, state_hist
