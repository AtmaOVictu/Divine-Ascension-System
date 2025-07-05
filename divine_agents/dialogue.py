from typing import List
from .agent import Agent
from .shadows import UrgentShadow
from .axis import SecondTrueAxis


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


def complex_dialogue(agent1: Agent, agent2: Agent, shadow: UrgentShadow, axis: SecondTrueAxis) -> List[str]:
    """Dialogue influenced by an urgent shadow and directional axis."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    shadow.trigger(agent1)
    shadow.trigger(agent2)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    dir1 = axis.determine_direction()
    dir2 = axis.determine_direction()
    lines.append(f"{agent1.name} smer: {dir1}")
    lines.append(f"{agent2.name} smer: {dir2}")

    lines.append(f"{agent1.name}: {agent1.respond('Kako vidiš resnico?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kako vidiš resnico?')}")
    return lines
