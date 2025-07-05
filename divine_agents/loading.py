from __future__ import annotations

from time import sleep

from .agent import Agent


def simulate_loading(agent: Agent, delay: float = 0.5) -> list[str]:
    """Simulate a simple loading sequence for an agent."""
    stages = ["Starting", "Initializing", "Emotion Update", "State Transition", "Completion"]
    outputs: list[str] = []
    for stage in stages:
        outputs.append(f"Loading: {stage}")
        if delay:
            sleep(delay)
        agent.transition()
        outputs.append(f"Current State: {agent.state}")
    outputs.append("System Loaded Successfully!")
    return outputs
