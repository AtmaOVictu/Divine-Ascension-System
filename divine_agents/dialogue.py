from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    prev = agent1.state
    agent1.transition()
    if agent1.state != prev:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6)
    prev = agent2.state
    agent2.transition()
    if agent2.state != prev:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Engage agents in a multi-turn philosophical debate."""
    transcript: List[str] = []

    for _ in range(rounds):
        transcript.extend(philosophical_dialogue(agent1, agent2))

    return transcript
