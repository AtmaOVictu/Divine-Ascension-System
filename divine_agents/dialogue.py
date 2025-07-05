from __future__ import annotations

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.philosopher.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.philosopher.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def simulate_loading(agent: Agent) -> List[str]:
    """Simulate a loading process during agent initialization and transitions."""
    steps = [
        "Starting",
        "Initializing",
        "Emotion Update",
        "State Transition",
        "Completion",
    ]
    output: List[str] = []
    for step in steps:
        output.append(f"Loading: {step}")
        agent.transition()
        output.append(f"Current State: {agent.philosopher.state}")
    output.append("System Loaded Successfully!")
    return output
