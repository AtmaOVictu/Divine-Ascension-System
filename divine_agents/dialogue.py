from typing import List
from .agent import Agent
from .nano_mega import NanoMoment, MegaMoment


def opposite_necessity(agent1: Agent, agent2: Agent) -> None:
    """Increase tension if agents hold opposing ontological views."""
    if agent1.state != agent2.state:
        agent1.update_tension(agent1.tension + 0.5)
        agent2.update_tension(agent2.tension + 0.5)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Introduce nano moments
    nano_a1 = NanoMoment(0.8)
    nano_a2 = NanoMoment(0.6)
    nano_a1.apply(agent1)
    nano_a2.apply(agent2)

    # Apply opposite necessity increasing tensions
    opposite_necessity(agent1, agent2)

    # Accumulate nano moments and potentially trigger mega transition
    mega = MegaMoment()
    mega.accumulate(nano_a1)
    mega.accumulate(nano_a2)
    mega.trigger(agent1)
    mega.trigger(agent2)

    # Ensure state transitions based on updated tension
    agent1.transition()
    agent2.transition()

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final responses
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
