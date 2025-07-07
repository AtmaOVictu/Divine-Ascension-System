"""Utilities for simulating philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agent1 reacts with anger which increases tension and causes a transition
    agent1.update_emotion(0.6, name="jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")

    # Agent2 stays calm initially
    agent2.update_emotion(0.4, name="veselje")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # After hearing agent1, agent2 becomes more emotional and transitions
    agent2.update_emotion(0.7, name="veselje")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
