"""Utilities to create philosophical dialogues between agents."""

from typing import List
from .agent import Agent, OntologicalState


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Opening statements based on current ontological states
    lines.append(
        f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise during the discussion
    agent1.update_emotion(0.6, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, "fear")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Closing statements after transitions
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
