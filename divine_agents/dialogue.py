from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical exchange with emotional feedback."""
    lines: List[str] = []

    # Initial viewpoints
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally to the discussion
    agent1.update_emotion(0.8)
    agent1.decay_tension()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    agent2.decay_tension()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Follow-up statements influenced by their emotions
    lines.append(f"{agent1.name}: {agent1.philosophical_answer()}")
    lines.append(f"{agent2.name}: {agent2.philosophical_answer()}")
    return lines
