from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a brief conversation illustrating ontological perspectives.

    The function demonstrates how two agents evolve during discussion. Each
    agent responds to the question "Kaj je resnica?" based on its current
    state. Emotional updates increase internal tension, triggering transitions
    from ``Ego`` to ``Jaz`` or from ``Jaz`` to ``Enotnost`` when thresholds are
    crossed. The returned list of lines records both the spoken dialogue and
    any state changes that occur.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
