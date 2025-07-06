from typing import List

from .emotional_agent import EmotionalAgent


def philosophical_dialogue(agent1: EmotionalAgent, agent2: EmotionalAgent) -> List[str]:
    """Simulate a philosophical dialogue influenced by emotions."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.set_emotion("strah", 0.6)
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_state} in prehaja v stanje: {agent1.transition()}"
    )

    agent2.set_emotion("veselje", 0.8)
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_state} in prehaja v stanje: {agent2.transition()}"
    )

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
