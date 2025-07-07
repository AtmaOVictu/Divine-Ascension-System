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


def dynamic_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue where emotions drive state transitions."""
    log = []
    log.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    log.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # first round of emotions
    agent1.apply_emotion('fear')
    log.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.apply_emotion('anger')
    log.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # second round responses
    log.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    log.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return log
