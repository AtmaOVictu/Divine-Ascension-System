from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each agent states their view of truth, emotions rise, and transitions may
    occur based on the predefined thresholds. The resulting conversation is
    returned as a list of lines.
    """
    lines: List[str] = []

    # Initial statements based on current state
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions escalate during the debate
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    # Agents attempt state transitions after the emotional exchange
    new_state1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")

    new_state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    # Final statements in their possibly new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
