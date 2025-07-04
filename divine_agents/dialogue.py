from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a multi-round philosophical dialogue between two agents."""
    log: List[str] = []
    for i in range(rounds):
        log.append(f"Krog {i + 1}:")
        log.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        log.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotions to drive transitions
        agent1.update_emotion("anger", 0.5)
        log.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion("fear", 0.5)
        log.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return log
