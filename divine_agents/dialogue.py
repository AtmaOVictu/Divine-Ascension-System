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


def debate(agent1: Agent, agent2: Agent, turns: int = 3) -> List[str]:
    """Conduct a multi-turn debate where emotions trigger transitions."""
    log: List[str] = []
    for _ in range(turns):
        # Each agent answers from its current ontological perspective
        log.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        # Hearing the other's view increases emotion and tension
        agent2.update_emotion(0.4)
        log.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        agent1.update_emotion(0.3)

        # State transitions may occur after emotions are updated
        log.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        log.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return log
