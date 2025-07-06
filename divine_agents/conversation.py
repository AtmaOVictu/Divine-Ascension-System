from typing import List
from .agent import Agent


def emotional_conversation(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate dialogue where emotions influence transitions."""
    lines = []
    # Initial views
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 experiences fear and surpasses threshold -> transition
    agent1.update_emotion(0.6, 'strah')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 experiences joy but below threshold
    agent2.update_emotion(0.4, 'veselje')
    lines.append(f"{agent2.name} ostaja v stanju: {agent2.transition()}")

    # Increase agent2 tension to trigger transition
    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
