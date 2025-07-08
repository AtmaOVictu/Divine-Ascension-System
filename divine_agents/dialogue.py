from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, decay_rate: float = 0.1) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial responses based on current state
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional updates trigger transitions
    agent1.update_emotion(0.8)
    agent1.transition()
    agent1.decay_tension(decay_rate)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6)
    agent2.transition()
    agent2.decay_tension(decay_rate)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final reflections after transition and decay
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
