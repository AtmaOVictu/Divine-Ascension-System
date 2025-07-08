from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    question = "Kaj je resnica?"
    lines = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # Emotional reactions influence tension and may trigger transitions
    agent1.update_emotion("anger", 0.8)
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_name} in prehaja v stanje: {agent1.transition()}"
    )

    agent2.update_emotion("joy", 0.8)
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_name} in prehaja v stanje: {agent2.transition()}"
    )

    # Final reflections in new states
    lines.append(f"{agent1.name}: {agent1.respond(question)}")
    lines.append(f"{agent2.name}: {agent2.respond(question)}")

    return lines
