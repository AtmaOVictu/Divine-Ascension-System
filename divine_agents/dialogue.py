from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where agents evolve emotionally."""
    lines: List[str] = []

    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Agents react emotionally to each round
        if i == 0:
            agent1.update_emotion(0.6, "anger")
            agent2.update_emotion(0.4, "fear")
        else:
            agent1.update_emotion(0.4, "joy")
            agent2.update_emotion(0.6, "joy")

        # transitions based on updated emotional states
        agent1_state = agent1.transition()
        agent2_state = agent2.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {agent1_state}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2_state}")

    # final responses after evolution
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
