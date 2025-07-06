from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical debate influenced by emotional states."""
    lines: List[str] = []
    for turn in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        if turn == 0:
            agent1.update_emotion(0.8, 'anger')
            agent1.add_experience('selfish')
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
            agent2.update_emotion(0.6, 'joy')
            agent2.add_experience('unifying')
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
        else:
            agent1.update_emotion(0.6, 'curious')
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.multi_layer_transition()}")
            agent2.update_emotion(0.4, 'thoughtful')
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.multi_layer_transition()}")

    return lines
