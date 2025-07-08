from typing import List
from .agent import Agent
from .retrieval import VectorStore


def philosophical_dialogue(agent1: Agent, agent2: Agent, store: VectorStore) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond_with_context('Kaj je resnica?', store)}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond_with_context('Kaj je resnica?', store)}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"{agent1.name}: {agent1.respond_with_context('Kaj je resnica?', store)}"
    )
    lines.append(
        f"{agent2.name}: {agent2.respond_with_context('Kaj je resnica?', store)}"
    )
    return lines
