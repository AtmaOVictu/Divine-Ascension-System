from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial statements
    lines.append(agent1.respond("What is truth?"))
    lines.append(agent2.respond("What is truth?"))

    # Agents react emotionally which may trigger transitions
    agent1.feel(anger=0.2)
    agent1.update_tension(0.8)
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

    agent2.feel(fear=0.3)
    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    # Final statements after learning
    lines.append(agent1.respond("How do you see truth now?"))
    lines.append(agent2.respond("How do you see truth now?"))

    agent1.learn_from_history()
    agent2.learn_from_history()

    return lines
