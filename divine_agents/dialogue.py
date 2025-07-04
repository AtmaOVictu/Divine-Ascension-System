from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The function updates emotional states which may trigger state transitions
    according to predefined thresholds.
    """
    lines: List[str] = []

    # Initial statements about truth.
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the debate influencing their tension.
    agent1.update_emotion('anger', 0.6)
    lines.append(f"{agent1.name} čuti {agent1.emotion_type} in prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion('joy', 0.6)
    lines.append(f"{agent2.name} čuti {agent2.emotion_type} in prehaja v stanje: {agent2.transition()}")

    # Final statements after emotional change and potential transition.
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
