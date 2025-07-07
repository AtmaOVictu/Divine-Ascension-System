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


from .ontology import DEEP_THOUGHT_LANGUAGE


def deep_thought_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue in deep thought mode using ontological symbols."""
    lines = []
    symbol = DEEP_THOUGHT_LANGUAGE.symbolism
    lines.append(
        f"{symbol['initiate']} {agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_tension(0.75)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"{symbol['transform']} {agent1.name}: {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    lines.append(symbol["resolve"])
    return lines
