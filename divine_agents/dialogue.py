"""Dialogue utilities for agent interactions wrapped in symbolic boxes."""

from typing import List

from .agent import Agent
from .symbolic_box import (
    SymbolicBox,
    initiate_task_with_box,
    process_task_with_box,
    resolve_task_with_box,
)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    box: SymbolicBox = initiate_task_with_box("philosophical_dialogue")
    process_task_with_box(box, "initial exchange")

    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    resolve_task_with_box(box)
    return lines
