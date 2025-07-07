from typing import List
from .agent import Agent
from .box import (
    SymbolicBox,
    initiate_task_with_box,
    process_task_with_box,
    resolve_task_with_box,
)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents using a symbolic box."""
    convo_box: SymbolicBox = initiate_task_with_box("philosophical_dialogue")

    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # emotions escalate during discussion
    agent1.update_emotion(0.8, emotion_type="anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, emotion_type="joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    process_task_with_box(convo_box, "dialogue progressed")
    convo_box.update_data({"lines": lines})
    resolve_task_with_box(convo_box)
    return lines
