from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The function updates the emotional state of each agent and triggers
    possible transitions based on the defined thresholds.
    """
    lines: List[str] = []

    emotion_sequence = [
        ("anger", 0.6, "joy", 0.4),
        ("joy", 0.6, "fear", 0.8),
    ]

    for e1, v1, e2, v2 in emotion_sequence:
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(e1, v1)
        agent2.update_emotion(e2, v2)
        lines.append(f"{agent1.name} čuti {e1} (intenziteta {v1})")
        lines.append(f"{agent2.name} čuti {e2} (intenziteta {v2})")

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
