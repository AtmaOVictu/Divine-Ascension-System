from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotion."""

    lines: List[str] = []

    # Initial exchange based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the discussion
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    # State transitions may occur due to heightened tension/emotion
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again from their potentially new state
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako zdaj razumeš resnico?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Se strinjaš?')}")

    return lines
