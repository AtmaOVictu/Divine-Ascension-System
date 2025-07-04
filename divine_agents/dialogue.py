from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements based on current state
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions influence the debate
    agent1.apply_emotion("anger")
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_label} in prehaja v stanje: {agent1.transition()}"
    )

    agent2.apply_emotion("joy")
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_label} in prehaja v stanje: {agent2.transition()}"
    )

    # Agent1 experiences additional emotion leading towards Enotnost
    agent1.apply_emotion("fear")
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_label} in prehaja v stanje: {agent1.transition()}"
    )

    # Responses after emotional impact
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
