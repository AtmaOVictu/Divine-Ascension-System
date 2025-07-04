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


def debate_truth(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a debate where emotions may trigger state transitions."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.6)
    previous_state = agent1.state
    state = agent1.transition()
    if state != previous_state:
        lines.append(f"{agent1.name} prehaja v stanje: {state}")

    agent2.update_emotion(0.8)
    previous_state = agent2.state
    state = agent2.transition()
    if state != previous_state:
        lines.append(f"{agent2.name} prehaja v stanje: {state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica sedaj?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica sedaj?')}")
    return lines
