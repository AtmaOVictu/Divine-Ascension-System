from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where emotions drive state changes."""

    lines: List[str] = []

    for i in range(rounds):
        question = "Kaj je resnica?" if i == 0 else "Kako vidiš resnico?"
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        # Modify emotions to potentially trigger transitions
        if i == 0:
            agent1.update_emotion("anger", 0.6)
            agent2.update_emotion("joy", 0.4)
        else:
            agent1.update_emotion("fear", 0.8)
            agent2.update_emotion("joy", 0.7)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections after all transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je koncna resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je koncna resnica?')}")

    return lines
