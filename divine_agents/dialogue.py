from typing import List
from .agent import Agent


def _react(listener: Agent, statement: str) -> str:
    """Adjust listener's emotion and tension based on a statement."""
    if "absolutna" in statement:
        delta = 0.3
    elif "relativna" in statement:
        delta = 0.2
    else:
        delta = 0.1
    listener.update_emotion(min(1.0, listener.emotion + delta))
    return listener.transition()


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate an emotional philosophical dialogue with state updates."""
    lines: List[str] = []

    for _ in range(3):
        statement1 = agent1.respond("Kaj je resnica?")
        lines.append(
            f"{agent1.name} ({agent1.state}, e={agent1.emotion:.2f}, t={agent1.tension:.2f}): {statement1}"
        )
        state2 = _react(agent2, statement1)
        lines.append(
            f"{agent2.name} -> {state2} (e={agent2.emotion:.2f}, t={agent2.tension:.2f})"
        )

        statement2 = agent2.respond("Kaj je resnica?")
        lines.append(
            f"{agent2.name} ({agent2.state}, e={agent2.emotion:.2f}, t={agent2.tension:.2f}): {statement2}"
        )
        state1 = _react(agent1, statement2)
        lines.append(
            f"{agent1.name} -> {state1} (e={agent1.emotion:.2f}, t={agent1.tension:.2f})"
        )

    return lines
