from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """A more elaborate debate using emotional transitions."""
    log = philosophical_dialogue(agent1, agent2)
    # Additional round where emotions cool down
    agent1.update_emotion(0.3, "joy")
    log.append(f"{agent1.name} umirja čustva: {agent1.transition()}")
    agent2.update_emotion(0.2, "neutral")
    log.append(f"{agent2.name} umirja čustva: {agent2.transition()}")
    log.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    log.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return log
