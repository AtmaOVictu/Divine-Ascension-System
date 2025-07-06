from typing import List
from .agent import Agent


def multi_turn_dialogue(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Run a multi-turn philosophical dialogue.

    Each round agents respond based on their ontological state. Their emotional
    intensity increases slightly, triggering transitions when thresholds are
    exceeded.
    """
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        
        agent1.update_emotion(0.3)
        agent2.update_emotion(0.3)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return lines
