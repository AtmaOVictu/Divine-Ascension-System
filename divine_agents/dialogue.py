from typing import List

from .agent import Agent
from .box import (
    initiate_task_with_box,
    process_task_with_box,
    resolve_task_with_box,
    SymbolicBox,
)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents using a symbolic box."""
    box: SymbolicBox = initiate_task_with_box("philosophical_dialogue")
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Process stage
    box = process_task_with_box(box, "initial exchange")

    # Emotional updates causing possible transitions
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    box = resolve_task_with_box(box)
    return lines
