from typing import List
from .agent import Agent


def emotional_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a dialogue where emotions drive state transitions."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # increase emotions, which in turn raises tension
        agent1.update_emotion(0.6)
        agent2.update_emotion(0.7)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return lines
