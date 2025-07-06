from typing import List
from .agent import Agent


def _dialogue_step(speaker: Agent) -> str:
    """Return a single line of dialogue for the speaker."""
    return f"{speaker.name} ({speaker.state}): {speaker.respond('Kaj je resnica?')}"


def philosophical_dialogue(agent1: Agent, agent2: Agent, inc1: float = 0.8, inc2: float = 0.6) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = [
        _dialogue_step(agent1),
        _dialogue_step(agent2),
    ]

    agent1.update_emotion(inc1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(inc2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(_dialogue_step(agent1))
    lines.append(_dialogue_step(agent2))
    return lines


def emotional_dialogue(agent1: Agent, agent2: Agent, inc1: float, inc2: float) -> List[str]:
    """Conduct a dialogue with configurable emotion increments."""
    return philosophical_dialogue(agent1, agent2, inc1, inc2)
