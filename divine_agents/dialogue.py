from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    # Initial exchange based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents experience emotions influencing their tension levels
    agent1.set_emotion("anger")
    lines.append(f"{agent1.name} čuti {agent1.emotion_name}.")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("fear")
    lines.append(f"{agent2.name} čuti {agent2.emotion_name}.")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Dialogue continues with updated states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
