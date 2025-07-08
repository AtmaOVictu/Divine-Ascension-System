from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue exposing contradictions."""
    lines: List[str] = []

    # Each agent expresses their fundamental belief
    agent1.add_belief("Truth is absolute")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")

    agent2.add_belief("Truth is relative")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents hear each other's statements and store them
    agent1.add_belief("Truth is relative")
    agent2.add_belief("Truth is absolute")

    # Detect and resolve contradictions
    lines.append(f"{agent1.name} zazna protislovja: {agent1.detect_contradictions()}")
    lines.append(f"{agent2.name} zazna protislovja: {agent2.detect_contradictions()}")

    agent1.resolve_contradictions()
    agent2.resolve_contradictions()

    # Reflection may trigger state transitions
    lines.append(f"{agent1.name} po razmisleku: {agent1.reflect()}")
    lines.append(f"{agent2.name} po razmisleku: {agent2.reflect()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
