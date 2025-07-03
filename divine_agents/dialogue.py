from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Engage agents in a dialogue where emotions influence transitions."""
    lines: List[str] = []

    # Initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Heighten emotions which may trigger transitions
    agent1.update_emotion(0.6, label='anger')
    lines.append(f"{agent1.name} čuti {agent1.emotion_label} in napetost {agent1.tension:.2f}")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, label='fear')
    lines.append(f"{agent2.name} čuti {agent2.emotion_label} in napetost {agent2.tension:.2f}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final exchange reflects new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
