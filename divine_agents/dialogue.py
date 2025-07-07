from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, language: str = "sl") -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    question = "What is truth?" if language == "en" else "Kaj je resnica?"
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question, language)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question, language)}")

    agent1.update_emotion("anger", 0.8, language)
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

    agent2.update_emotion("joy", 0.6, language)
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond(question, language)}")
    lines.append(f"{agent2.name}: {agent2.respond(question, language)}")
    return lines
