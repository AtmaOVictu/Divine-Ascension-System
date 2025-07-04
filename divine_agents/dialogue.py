from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # First emotion: agent1 experiences anger
    agent1.apply_emotion("anger")
    lines.append(f"{agent1.name} čuti {agent1.emotion_label} in prehaja v stanje: {agent1.transition()}")

    # Second emotion: agent2 experiences joy
    agent2.apply_emotion("joy")
    lines.append(f"{agent2.name} čuti {agent2.emotion_label} in prehaja v stanje: {agent2.transition()}")

    # Third emotion: agent1 experiences sorrow
    agent1.apply_emotion("sorrow")
    lines.append(f"{agent1.name} čuti {agent1.emotion_label} in prehaja v stanje: {agent1.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
