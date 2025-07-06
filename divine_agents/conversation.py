from typing import List
from .agent import Agent


def dynamic_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Run a dynamic debate between two agents."""
    dialogue = []
    for _ in range(rounds):
        dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion('anger', agent1.emotion + 0.3)
        agent2.update_emotion('fear', agent2.emotion + 0.3)

        new_state1 = agent1.transition()
        new_state2 = agent2.transition()
        dialogue.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        dialogue.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    return dialogue
