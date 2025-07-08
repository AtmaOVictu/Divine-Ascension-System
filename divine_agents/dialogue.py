from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts with anger but below threshold
    agent1.set_emotion('anger', 0.4)
    lines.append(f"{agent1.name} se počuti {agent1.emotion_type}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako odgovoriš?')}")

    # Agent2 brings joyful argument, crossing threshold and transitioning
    agent2.set_emotion('joy', 0.6)
    new_state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako odgovoriš?')}")

    # Agent1 softens and moves towards Jaz
    agent1.set_emotion('sorrow', 0.8)
    new_state1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica zdaj?')}")

    return lines
