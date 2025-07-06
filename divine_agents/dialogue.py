from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial viewpoints
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions escalate during the debate
    agent1.update_emotion('anger')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 feels fear and may ascend to a higher state
    agent2.update_emotion('fear')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # After transitions, agents respond again
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
