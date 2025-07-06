from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions arise during the debate
    agent1.feel('anger')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.feel('fear')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    agent2.feel('anger')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Subsequent statements reflect new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj pa zdaj?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj pa zdaj?')}")
    return lines


def dynamic_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Conduct a dialogue with escalating emotions leading to transitions."""
    conversation = philosophical_dialogue(agent1, agent2)
    # After the first exchange, intensify emotions
    agent1.feel('fear')
    agent2.feel('anger')
    agent1.transition()
    agent2.transition()
    conversation.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaksna je absolutna resnica?')}")
    conversation.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaksna je relativna resnica?')}")
    return conversation
