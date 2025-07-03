from typing import List
from .agent import Agent


def _adjust_emotion(listener: Agent, statement: str) -> None:
    """Update listener's emotion based on the speaker's statement."""
    delta = 0.1
    if "absolutna" in statement and listener.state != "Ego":
        delta = 0.8
    elif "relativna" in statement and listener.state != "Jaz":
        delta = 0.8
    elif "eno" in statement and listener.state != "Enotnost":
        delta = 0.8

    new_emotion = min(1.0, listener.emotion + delta)
    listener.update_emotion(new_emotion)
    listener.transition()


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue with emotional dynamics."""
    lines: List[str] = []

    # Agent1 speaks first
    statement1 = agent1.respond("Kaj je resnica?")
    lines.append(
        f"{agent1.name} ({agent1.state}, e={agent1.emotion:.2f}, t={agent1.tension:.2f}): {statement1}"
    )
    _adjust_emotion(agent2, statement1)
    lines.append(
        f"{agent2.name} -> {agent2.state} e={agent2.emotion:.2f} t={agent2.tension:.2f}"
    )

    # Agent2 responds
    statement2 = agent2.respond("Kaj je resnica?")
    lines.append(
        f"{agent2.name} ({agent2.state}, e={agent2.emotion:.2f}, t={agent2.tension:.2f}): {statement2}"
    )
    _adjust_emotion(agent1, statement2)
    lines.append(
        f"{agent1.name} -> {agent1.state} e={agent1.emotion:.2f} t={agent1.tension:.2f}"
    )

    # Final reflections after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
