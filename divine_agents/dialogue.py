from typing import List

from .agent import Agent
from .states import philosophy_response


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical debate between two agents."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}")
        # escalate emotions slightly during debate
        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.2))
        if agent1.transition_if_needed():
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state.value}")
        if agent2.transition_if_needed():
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state.value}")
    # final statements after possible transitions
    lines.append(
        f"{agent1.name} ({agent1.state.value}): {philosophy_response(agent1.state)}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state.value}): {philosophy_response(agent2.state)}"
    )
    return lines
