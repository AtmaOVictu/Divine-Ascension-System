from typing import List
from .agent import Agent
from .generator import Generator


def philosophical_dialogue(agent1: Agent, agent2: Agent, generator: Generator | None = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # generator may increase emotion/tension
    if generator:
        generator.stimulate(agent1)
        generator.stimulate(agent2)

    # apply transitions after stimulation
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # follow-up responses reflecting new states and emotions
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
