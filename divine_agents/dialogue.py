from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a multi-turn dialogue where emotions influence transitions."""
    log: List[str] = []
    for _ in range(rounds):
        log.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        log.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(min(1.0, agent1.emotion + 0.4),
                              'jeza' if agent1.state == 'Ego' else 'veselje')
        agent2.update_emotion(min(1.0, agent2.emotion + 0.4),
                              'radovednost' if agent2.state == 'Jaz' else 'mirnost')

        log.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        log.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return log
