from typing import List
from .agent import Agent
from .retrieval import build_index, search

PHILOSOPHY_TEXTS = [
    "Resnica je absolutna in neodvisna od drugih.",
    "Resnica je relativna, oblikovana z našimi odnosi.",
    "Vse resnice so eno, medsebojno povezane."
]
INDEX = build_index(PHILOSOPHY_TEXTS)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    context = ", ".join(search("resnica", INDEX, top_k=2))
    lines.append(f"Spomin: {context}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
