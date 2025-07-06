from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.set_emotion_state('anger', 0.8)
    lines.append(f"{agent1.name} čuti {agent1.emotion_state} in prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion_state('fear', 0.6)
    lines.append(f"{agent2.name} čuti {agent2.emotion_state} in prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def emotional_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Dialogue showcasing emotional states affecting transitions."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.set_emotion_state('anger', 0.9)
    lines.append(f"{agent1.name} čuti {agent1.emotion_state} in prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion_state('joy', 0.4)
    lines.append(f"{agent2.name} čuti {agent2.emotion_state} in prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
