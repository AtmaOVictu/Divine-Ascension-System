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


def ontological_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a debate where emotions influence state transitions."""
    dialogue = []

    # Initial statements about truth
    dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reaction: Agent1 becomes tense after hearing Agent2
    agent1.update_emotion(0.6)
    dialogue.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 responds with empathy raising its own emotion slightly
    agent2.update_emotion(0.4)
    dialogue.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of answers reflecting new states
    dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return dialogue
