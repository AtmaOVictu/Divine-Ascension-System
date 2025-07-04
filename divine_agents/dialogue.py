from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue with emotional influences."""

    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 becomes angry which raises tension enough to transition
    agent1.update_emotion(0.6, "anger")
    lines.append(f"{agent1.name} čuti jezo. Prehod v stanje: {agent1.transition()}")

    # Agent2 is joyful but not enough for transition yet
    agent2.update_emotion(0.4, "joy")
    lines.append(f"{agent2.name} čuti veselje. Prehod v stanje: {agent2.transition()}")

    # Agent2 increases emotion again leading to transition to Enotnost
    agent2.update_emotion(0.8, "joy")
    lines.append(f"{agent2.name} okrepi veselje. Prehod v stanje: {agent2.transition()}")

    # Final reflections
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
