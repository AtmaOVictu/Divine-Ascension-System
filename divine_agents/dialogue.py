from typing import List
from .agent import Agent
from .advanced_agents import (
    ReasonAgent,
    InterpolationAgent,
    IntercontinentalizationAgent,
)


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


def extended_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Extended dialogue including advanced agents."""
    lines = philosophical_dialogue(agent1, agent2)

    reasoner = ReasonAgent("Razum", logic_level=0.8)
    lines.append(reasoner.reason("dialogue"))

    interpolator = InterpolationAgent("Interp", interpolation_level=0.8)
    lines.append(interpolator.interpolate(agent1, agent2))

    intercontinental = IntercontinentalizationAgent("Intercon", reach=0.8)
    lines.append(intercontinental.connect_worlds(agent1, agent2))

    return lines
