"""Utilities for simulating philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short dialogue highlighting state transitions.

    The conversation evolves in two rounds. After the first exchange each agent
    experiences emotions which may trigger a state change. A second exchange
    then reflects the updated philosophical stances. Finally, emotions escalate
    once more, potentially leading to the final ontological phase.
    """

    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # first emotional shift and possible transition
    agent1.update_emotion(0.8, 'anger')
    agent2.update_emotion(0.6, 'joy')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # second round of statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # escalate again to reach higher phases if possible
    agent1.update_emotion(0.8, 'joy')
    agent2.update_emotion(0.8, 'anger')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
