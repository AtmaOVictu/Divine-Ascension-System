from typing import List
from .agent import Agent


def _format_line(agent: Agent, question: str) -> str:
    """Helper to format a dialogue line."""
    return f"{agent.name} ({agent.state}): {agent.respond(question)}"


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = [
        _format_line(agent1, "Kaj je resnica?"),
        _format_line(agent2, "Kaj je resnica?")
    ]

    # Agents react emotionally to each other's statements
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(_format_line(agent1, "Kaj je resnica?"))
    lines.append(_format_line(agent2, "Kaj je resnica?"))
    return lines
