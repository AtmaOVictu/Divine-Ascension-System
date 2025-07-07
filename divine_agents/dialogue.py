"""Dialogue utilities for philosophical agents."""

from typing import List
from .agent import Agent


def _influence_emotion(speaker: Agent, listener: Agent) -> None:
    """Update the listener's emotion and tension in response to a statement."""
    # Emotional impact values depend on the speaker's ontological state. The
    # impact is intentionally strong to trigger transitions during testing.
    impact_map = {"Ego": 0.8, "Jaz": 0.6, "Enotnost": 0.6}
    impact = impact_map.get(speaker.state, 0.0)
    listener.update_emotion(listener.emotion + impact)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Each statement influences the listener's emotional state which may lead to
    a transition. The dialogue showcases absolute, relative and unified truths
    depending on the agents' states.
    """

    lines: List[str] = []

    # Agent1 makes an initial statement about truth (likely absolute).
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    _influence_emotion(agent1, agent2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agent2 responds from their (possibly new) state.
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    _influence_emotion(agent2, agent1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Final reflections after transitions.
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
