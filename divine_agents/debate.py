"""Utilities for simulating dynamic philosophical debates between agents."""

from typing import List

from .agent import Agent
from .utils import sanitize_output


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a debate where emotions may cause state transitions."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agent1 feels fear after agent2's argument
    agent1.update_emotion(0.6, "fear")
    lines.append(sanitize_output(f"{agent1.name} čuti strah."))
    if agent1.transition() != agent1.history[-2]:
        lines.append(
            sanitize_output(f"{agent1.name} prehaja v stanje: {agent1.state}")
        )

    # Agent2 reacts with joy
    agent2.update_emotion(0.4, "joy")
    lines.append(sanitize_output(f"{agent2.name} čuti veselje."))
    if agent2.transition() != agent2.history[-2]:
        lines.append(
            sanitize_output(f"{agent2.name} prehaja v stanje: {agent2.state}")
        )

    # Final responses after emotional shifts
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines

