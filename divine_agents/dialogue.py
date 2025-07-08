from typing import List

from .agent import Agent
from .philosophy import (
    handle_complex_query,
    parse_philosophical_statement,
    self_reflection,
)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial responses
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Store statements for later reflection
    parse_philosophical_statement("Kaj je resnica?", agent1.memory)
    parse_philosophical_statement("Kaj je resnica?", agent2.memory)

    # Emotional shifts
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Handle complex query as part of conversation
    lines.append(handle_complex_query("paradox", agent1.memory))

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # Agents reflect on dialogue
    lines.append(self_reflection(agent1.memory))
    lines.append(self_reflection(agent2.memory))

    return lines
