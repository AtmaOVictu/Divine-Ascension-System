from __future__ import annotations

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_debate(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Simulate a debate where agents may transition states based on emotions."""
    transcript: List[str] = []

    for _ in range(turns):
        transcript.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        transcript.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(0.6, "anger")
        prev1 = agent1.state
        agent1.transition()
        if prev1 != agent1.state:
            transcript.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

        agent2.update_emotion(0.6, "joy")
        prev2 = agent2.state
        agent2.transition()
        if prev2 != agent2.state:
            transcript.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return transcript
