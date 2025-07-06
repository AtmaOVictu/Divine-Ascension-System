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


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a deterministic debate demonstrating emotional influence and transitions."""
    dialogue = []

    # Initial statements
    dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # First emotional wave
    agent1.update_emotion(0.6)
    prev_state = agent1.state
    agent1.transition()
    if prev_state != agent1.state:
        dialogue.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.4)
    prev_state = agent2.state
    agent2.transition()
    if prev_state != agent2.state:
        dialogue.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Second emotional wave
    agent1.update_emotion(0.2)
    agent2.update_emotion(0.7)

    prev_state = agent1.state
    agent1.transition()
    if prev_state != agent1.state:
        dialogue.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    prev_state = agent2.state
    agent2.transition()
    if prev_state != agent2.state:
        dialogue.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return dialogue
