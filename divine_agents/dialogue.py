from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Opening statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional responses influence transitions
    agent1.update_emotion("anger", 0.6)
    new_state1 = agent1.transition()
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_type} in prehaja v stanje: {new_state1}"
    )

    agent2.update_emotion("joy", 0.8)
    new_state2 = agent2.transition()
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_type} in prehaja v stanje: {new_state2}"
    )

    # Second round of arguments with updated states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Ali obstaja resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Ali obstaja resnica?')}"
    )
    return lines
