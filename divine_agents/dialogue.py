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

from .multicolor_agent import MultiColorAgent


def colorful_dialogue(agent1: MultiColorAgent, agent2: MultiColorAgent) -> List[str]:
    """Simulate dialogue including color and visibility information."""
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}/{agent1.current_color()}/{agent1.current_visibility()}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}/{agent2.current_color()}/{agent2.current_visibility()}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(
        f"{agent1.name} prehaja v stanje: {agent1.transition()} ({agent1.current_color()})"
    )

    agent2.update_emotion(0.6)
    lines.append(
        f"{agent2.name} prehaja v stanje: {agent2.transition()} ({agent2.current_color()})"
    )

    lines.append(
        f"{agent1.name}: {agent1.respond('Kaj je resnica?')} ({agent1.current_color()})"
    )
    lines.append(
        f"{agent2.name}: {agent2.respond('Kaj je resnica?')} ({agent2.current_color()})"
    )
    return lines
