from typing import List
from .agent import Agent, OntologicalState


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition().value}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition().value}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Conduct a multi-step dialogue where emotions drive state changes."""
    dialogue: List[str] = []
    rounds = [(0.4, 0.6), (0.4, 0.2)]

    for emo1, emo2 in rounds:
        dialogue.append(
            f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}"
        )
        dialogue.append(
            f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(emo1)
        agent2.update_emotion(emo2)

        dialogue.append(f"{agent1.name} prehaja v stanje: {agent1.transition().value}")
        dialogue.append(f"{agent2.name} prehaja v stanje: {agent2.transition().value}")

    dialogue.append(
        f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}"
    )
    dialogue.append(
        f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}"
    )
    return dialogue
