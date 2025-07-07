from typing import List
from .agent import Agent


def dynamic_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a multi-round philosophical debate between two agents.

    Each round both agents respond according to their current state. Their
    emotion is increased which may cause tension to exceed thresholds and
    trigger state transitions. Dialogue lines as well as transition messages
    are returned for inspection or display.
    """
    lines: List[str] = []
    for _ in range(rounds):
        # Agents express their current understanding of truth
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotions intensify which affects tension
        agent1.update_emotion(0.4)
        agent2.update_emotion(0.4)

        # Perform possible state transitions
        new_state1 = agent1.transition()
        new_state2 = agent2.transition()

        lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

        # Respond again after transition to show changed perspective
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
