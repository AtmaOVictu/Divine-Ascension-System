from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    question = "Kaj je resnica?"
    lines: List[str] = []

    # Initial responses based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # Increase emotional intensity to trigger possible transitions
    agent1.update_emotion(agent1.emotion + 0.6)
    agent2.update_emotion(agent2.emotion + 0.6)

    # Apply transitions if thresholds are met
    prev1 = agent1.state
    prev2 = agent2.state
    agent1.transition()
    agent2.transition()

    if prev1 != agent1.state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if prev2 != agent2.state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final reflections after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines
