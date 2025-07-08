from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate reflecting emotional state changes."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # emotions rise during discussion
    agent1.feel("anger", 0.8)
    lines.append(f"{agent1.name} čuti {agent1.emotion_name}; prehaja v stanje: {agent1.transition()}")

    agent2.feel("joy", 0.6)
    lines.append(f"{agent2.name} čuti {agent2.emotion_name}; prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
