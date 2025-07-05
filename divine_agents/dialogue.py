"""Utilities to orchestrate philosophical dialogue between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Agents respond according to their current ontological and emotional states.
    Emotions are updated as the debate progresses, potentially triggering
    state transitions.
    """

    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts emotionally to agent2's argument
    agent1.update_emotion(0.6, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 responds with joy, possibly reaching unity
    agent2.update_emotion(0.8, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final responses after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
