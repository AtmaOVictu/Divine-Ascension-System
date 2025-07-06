from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""

    lines: List[str] = []

    # Initial positions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the debate
    agent1.update_emotion(0.8, label="angry")
    agent1.add_experience("selfish argument")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.multi_layer_transition()}")

    agent2.update_emotion(0.6, label="fearful")
    agent2.loyalty = 0.9
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.multi_layer_transition()}")

    # Second exchange after transitions
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
