from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8, "jeza")
    prev = agent1.state
    agent1.transition()
    if agent1.state != prev:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6, "veselje")
    prev = agent2.state
    agent2.transition()
    if agent2.state != prev:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Longer debate where emotions influence state transitions."""
    transcript: List[str] = []

    transcript.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    transcript.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agent1 reacts strongly to Agent2's argument
    agent1.update_emotion(0.6, "strah")
    prev = agent1.state
    agent1.transition()
    if agent1.state != prev:
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    # Agent2 remains calm but thoughtful
    agent2.update_emotion(0.4, "mir")
    prev = agent2.state
    agent2.transition()
    if agent2.state != prev:
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    transcript.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    transcript.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return transcript
