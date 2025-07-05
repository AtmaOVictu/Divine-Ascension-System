from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The agents exchange views on truth. Their emotional state is updated during
    the interaction which may trigger state transitions.
    """
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions escalate during debate
    agent1.update_emotion(0.8, "jeza")
    new_state1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")

    agent2.update_emotion(0.6, "radost")
    new_state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    # Second round of statements after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
