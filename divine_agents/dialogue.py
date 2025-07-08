from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate influenced by emotions."""
    lines: List[str] = []

    # Initial statements about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?')}")

    # Emotional reactions and possible transitions
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

    agent2.update_emotion(0.7)
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    # Final reflections after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('And now?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('And now?')}")

    return lines
