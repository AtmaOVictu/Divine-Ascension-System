from typing import List, Optional
from .agent import Agent
from .semantics import VectorStore


def philosophical_dialogue(agent1: Agent, agent2: Agent, memory: Optional[VectorStore] = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents with semantic memory."""
    if memory is None:
        memory = VectorStore()
    lines: List[str] = []
    question = "Kaj je resnica?"

    l1 = f"{agent1.name} ({agent1.state}): {agent1.respond(question)}"
    l2 = f"{agent2.name} ({agent2.state}): {agent2.respond(question)}"
    lines.extend([l1, l2])
    memory.add_texts([l1, l2])

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    l3 = f"{agent1.name}: {agent1.respond(question)}"
    l4 = f"{agent2.name}: {agent2.respond(question)}"
    lines.extend([l3, l4])
    memory.add_texts([l3, l4])

    retrieved = memory.search("resnica", top_k=2)
    for text in retrieved:
        lines.append(f"[spomin] {text}")

    return lines
