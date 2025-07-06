from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The conversation heightens emotions and tension, potentially causing
    state transitions. The returned list contains each line spoken by the
    agents as well as notes on their transitions.
    """

    lines: List[str] = []

    # Initial exchange based on current states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise as the debate intensifies
    agent1.update_emotion(0.8)
    lines.append(
        f"{agent1.name} čuti čustva {agent1.emotion:.1f}, napetost {agent1.tension:.1f}"
    )
    state1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {state1}")

    agent2.update_emotion(0.6)
    lines.append(
        f"{agent2.name} čuti čustva {agent2.emotion:.1f}, napetost {agent2.tension:.1f}"
    )
    state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {state2}")

    # Final reflections with potentially new perspectives
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
