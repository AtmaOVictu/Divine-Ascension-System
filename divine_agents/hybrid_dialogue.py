"""Dialogue utilities for agents using evolution and superposition."""
from typing import List

from .agent import Agent
from .superpositional import SuperpositionalAgent


def hybrid_dialogue(e_agent: Agent, s_agent: SuperpositionalAgent) -> List[str]:
    """Simulate a dialogue between an evolutionary and a superpositional agent."""
    lines = []
    lines.append(f"{e_agent.name} ({e_agent.state}): {e_agent.respond('Kaj je resnica?')}")
    lines.append(f"{s_agent.name} ({s_agent.states[0]}): {s_agent.respond('Kaj je resnica?')}")

    e_agent.update_emotion(0.8)
    lines.append(f"{e_agent.name} prehaja v stanje: {e_agent.transition()}")

    s_agent.update_emotion(0.6)
    lines.append(f"{s_agent.name} prehaja v stanje: {s_agent.transition()}")

    lines.append(f"{e_agent.name}: {e_agent.respond('Kaj je resnica?')}")
    lines.append(f"{s_agent.name}: {s_agent.respond('Kaj je resnica?')}")
    return lines
