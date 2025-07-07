from typing import List
from .agent import Agent
from .symbolic import SymbolicBox, initiate_task, process_task, resolve_task


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> SymbolicBox:
    """Simulate a short philosophical dialogue between two agents."""
    box = initiate_task("dialogue")
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kako doživljaš resnico?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kako doživljaš resnico?')}")

    process_task(box, {"dialogue": lines})
    resolve_task(box)
    return box
