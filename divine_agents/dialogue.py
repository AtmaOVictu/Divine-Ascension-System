from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

from .boxes import SymbolicBox


def philosophical_dialogue_boxed(agent1: Agent, agent2: Agent) -> List[SymbolicBox]:
    """Run dialogue using symbolic boxes for each ontological stage."""
    boxes: List[SymbolicBox] = []

    # Initiation box (∴)
    start_lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]
    boxes.append(SymbolicBox(stage="∴", data={"dialogue": start_lines}))

    # Transformation box (∆)
    agent1.update_emotion(0.8)
    agent1.transition()
    agent2.update_emotion(0.6)
    agent2.transition()
    mid_lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]
    boxes.append(SymbolicBox(stage="∆", data={"dialogue": mid_lines}))

    # Resolution box (⊘)
    agent1.update_emotion(0.2)
    agent1.transition()
    agent2.update_emotion(0.2)
    agent2.transition()
    end_lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Zakljucek?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Zakljucek?')}",
    ]
    boxes.append(SymbolicBox(stage="⊘", data={"dialogue": end_lines}))

    return boxes
