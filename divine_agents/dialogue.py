from typing import List
from .agent import Agent
from .dynamics import EmotionalTensionDynamics


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.emotion = 'angry'
    EmotionalTensionDynamics(agent1).adjust_tension()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.emotion = 'fear'
    EmotionalTensionDynamics(agent2).adjust_tension()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
