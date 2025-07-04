import random
from typing import List

from .agent import Agent


def run_simulation(agent1: Agent, agent2: Agent, iterations: int = 5) -> List[str]:
    """Simulate agents transitioning states based on random emotion and tension."""
    lines = []
    for _ in range(iterations):
        for ag in (agent1, agent2):
            ag.update_emotion(random.random())
            ag.update_tension(random.random())
            previous = ag.state
            ag.transition()
            lines.append(
                f"{ag.name} prej {previous} zdaj {ag.state} "
                f"(čustvo={ag.emotion:.2f}, napetost={ag.tension:.2f})"
            )
            lines.append(f"{ag.name}: {ag.respond('Kaj je resnica?')}")
    return lines
