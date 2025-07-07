"""Utilities for simulating philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a simple philosophical exchange between two agents."""

    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines


def progressive_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a multi-round debate where emotions drive state transitions."""

    transcript: List[str] = []
    for _ in range(rounds):
        transcript.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        transcript.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # Emotions rise as debate continues.
        agent1.update_emotion(agent1.emotion + 0.4)
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.3)
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return transcript
