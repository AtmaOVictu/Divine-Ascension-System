from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short time-aware philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(
        f"[t={agent1.time}] {agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    agent1.advance_time()

    lines.append(
        f"[t={agent2.time}] {agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    agent2.advance_time()

    agent1.update_emotion(0.8)
    lines.append(f"[t={agent1.time}] {agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"[t={agent2.time}] {agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"[t={agent1.time}] {agent1.name}: {agent1.respond('Kaj je resnica?')}"
    )
    agent1.advance_time()
    lines.append(
        f"[t={agent2.time}] {agent2.name}: {agent2.respond('Kaj je resnica?')}"
    )
    agent2.advance_time()

    return lines
