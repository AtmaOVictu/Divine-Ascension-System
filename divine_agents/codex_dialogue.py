from typing import List

from .codex_agent import CodexAgent


def dynamic_dialogue(agent1: CodexAgent, agent2: CodexAgent) -> List[str]:
    """Conduct a short dialogue reflecting agents' states and transitions."""
    lines: List[str] = []
    question = "Kaj je resnica?"

    # Initial statements
    lines.append(f"{agent1.ime} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.ime} ({agent2.state}): {agent2.respond(question)}")

    # Emotional impact leading to transitions
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.ime} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8)
    lines.append(f"{agent2.ime} prehaja v stanje: {agent2.transition()}")

    # Responses after transition
    lines.append(f"{agent1.ime} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.ime} ({agent2.state}): {agent2.respond(question)}")

    return lines
