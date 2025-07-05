from typing import List
from .agent import Agent


def _react(agent: Agent, opponent_state: str) -> None:
    """Modify agent's emotion based on the opponent's current state."""
    if opponent_state == "Ego":
        agent.update_emotion(0.8, "jeza")
    elif opponent_state == "Jaz":
        agent.update_emotion(0.6, "radovednost")
    else:
        agent.update_emotion(0.6, "navdih")


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    _react(agent1, agent2.state)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    _react(agent2, agent1.state)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
