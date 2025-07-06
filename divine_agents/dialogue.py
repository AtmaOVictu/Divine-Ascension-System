from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines = []
    question = "Kaj je resnica?"

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # Emotional reactions modify tension which may trigger transitions
    agent1.feel("anger", 0.6)
    lines.append(f"{agent1.name} čuti {agent1.emotion_type}.")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.feel("joy", 0.8)
    lines.append(f"{agent2.name} čuti {agent2.emotion_type}.")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Updated statements after emotional shifts
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines
