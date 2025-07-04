from typing import List

from .agent import Agent


def debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical debate between two agents.

    After each exchange emotions increase which may trigger state transitions.
    """
    dialogue = []
    for _ in range(rounds):
        dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions and tension
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0))

        agent1.transition()
        agent2.transition()
    return dialogue
