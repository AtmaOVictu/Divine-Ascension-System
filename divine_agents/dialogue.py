from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial exchange based on their current ontological states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional shift and possible state transition for agent1
    agent1.set_emotion("fear", 0.6)
    lines.append(f"{agent1.name} čuti {agent1.emotion_name} in prehaja v stanje: {agent1.transition()}")

    # Emotional shift and possible state transition for agent2
    agent2.set_emotion("joy", 0.8)
    lines.append(f"{agent2.name} čuti {agent2.emotion_name} in prehaja v stanje: {agent2.transition()}")

    # Exchange after the transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
