from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # increase emotion and pathos to trigger transitions
    agent1.update_emotion(0.8)
    agent1.adjust_pathos(3)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    agent2.adjust_pathos(2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # synchronize pathos which might cause another transition
    agent1.sync_pathos()
    agent2.sync_pathos()

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
