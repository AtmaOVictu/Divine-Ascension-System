from typing import List
from .agent import Agent
from .reason_agent import ReasonAgent
from .interpolation_agent import InterpolationAgent
from .intercontinental_agent import IntercontinentalizationAgent


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


def extended_dialogue(agent1: Agent, agent2: Agent,
                       reason_agent: ReasonAgent,
                       interp_agent: InterpolationAgent,
                       intercon_agent: IntercontinentalizationAgent) -> List[str]:
    """Dialogue demonstrating advanced agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    lines.append(reason_agent.reason('narava resnice'))
    lines.append(interp_agent.interpolate(agent1, agent2))
    lines.append(intercon_agent.connect_worlds(agent1, agent2))

    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
