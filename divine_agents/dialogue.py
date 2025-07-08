from typing import List, Optional

from .agent import Agent
from .retrieval import VectorStore


def philosophical_dialogue(
    agent1: Agent, agent2: Agent, store: Optional[VectorStore] = None
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    If a ``store`` is provided, all dialogue lines are added for semantic
    retrieval.
    """
    lines: List[str] = []

    def record(text: str) -> None:
        lines.append(text)
        if store is not None:
            store.add(text)

    record(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    record(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    record(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    record(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    record(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    record(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
