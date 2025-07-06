from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial positions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent2's argument affects Agent1's emotions
    agent1.update_emotion(0.6, "jeza")
    lines.append(f"{agent1.name} čuti {agent1.emotion_name} in prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico?')}")

    # Agent1's shift influences Agent2
    agent2.update_emotion(0.6, "veselje")
    lines.append(f"{agent2.name} čuti {agent2.emotion_name} in prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako vidiš resnico?')}")

    return lines
