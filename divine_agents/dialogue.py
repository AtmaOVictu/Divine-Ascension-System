from typing import List
from .agent import Agent
from .emotion import Emotion


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.apply_emotion(Emotion("fear", 0.8))
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.apply_emotion(Emotion("joy", 0.6))
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Extended dialogue showcasing emotional circulation."""
    lines = philosophical_dialogue(agent1, agent2)

    agent1.apply_emotion(Emotion("anger", 0.7))
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")

    agent2.apply_emotion(Emotion("sorrow", 0.9))
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
