from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by coincidences."""

    lines: List[str] = []

    # Initial positions on truth
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Each agent experiences a happy coincidence during interaction
    event1 = agent1.interact_with(agent2)
    event2 = agent2.interact_with(agent1)
    lines.append(f"Coincidence for {agent1.name}: {event1}")
    lines.append(f"Coincidence for {agent2.name}: {event2}")

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Responses after the coincidences influence their states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
