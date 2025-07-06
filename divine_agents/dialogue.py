from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents."""
    lines: List[str] = []
    emotion_cycle1 = ["anger", "fear", "joy"]
    emotion_cycle2 = ["joy", "fear", "anger"]

    for i in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.set_emotion(emotion_cycle1[i % len(emotion_cycle1)], 0.4 + 0.2 * i)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.set_emotion(emotion_cycle2[i % len(emotion_cycle2)], 0.5 + 0.2 * i)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
