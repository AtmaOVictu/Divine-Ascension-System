import math
from typing import List

from .agent import Agent


def decay_tension(agent: Agent, time_step: float = 1.0) -> None:
    """Decay an agent's tension over time based on its emotion."""
    decay_rate = 0.1 + agent.emotion * 0.4
    agent.tension = agent.tension * math.exp(-decay_rate * time_step)


def reinforce(agent: Agent, reward: float) -> None:
    """Adjust agent's emotion and tension using a simple reward signal."""
    agent.tension = max(0.0, agent.tension - reward * 0.05)
    agent.emotion = min(1.0, max(0.0, agent.emotion + reward * 0.1))


def learning_cycle(agent1: Agent, agent2: Agent, steps: int = 5) -> List[str]:
    """Run a learning cycle with tension decay, transition and reinforcement."""
    log: List[str] = []
    for _ in range(steps):
        decay_tension(agent1)
        decay_tension(agent2)
        agent1.transition()
        agent2.transition()
        log.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        log.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        reward1 = 1.0 if agent1.state == 'Enotnost' else -1.0
        reward2 = 1.0 if agent2.state == 'Enotnost' else -1.0
        reinforce(agent1, reward1)
        reinforce(agent2, reward2)
    return log
