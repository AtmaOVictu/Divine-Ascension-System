from typing import List
from .agent import Agent
from .symbolic_box import SymbolicBox


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    box = SymbolicBox(stage="∴", data={"topic": "Kaj je resnica?"})
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(box.data['topic'])}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(box.data['topic'])}")

    box.transition("∆", {"stage": "discussion"})

    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond(box.data['topic'])}")
    lines.append(f"{agent2.name}: {agent2.respond(box.data['topic'])}")

    box.transition("⊘", {"status": "completed"})
    lines.append(str(box))
    return lines
