"""Utilities for conducting philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def dialogue_round(agent1: Agent, agent2: Agent, emotion_step: float = 0.3) -> List[str]:
    """Perform a single dialogue round and update agent states.

    Parameters
    ----------
    agent1 : Agent
        First participant.
    agent2 : Agent
        Second participant.
    emotion_step : float, optional
        Value added to both agents' emotion and tension each round.

    Returns
    -------
    List[str]
        Dialogue lines describing the interaction and state changes.
    """

    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]

    agent1.update_emotion(emotion_step)
    agent2.update_emotion(emotion_step)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2, emotion_step: float = 0.3) -> List[str]:
    """Simulate a multi-round philosophical dialogue between two agents."""
    transcript: List[str] = []
    for _ in range(rounds):
        transcript.extend(dialogue_round(agent1, agent2, emotion_step))

    transcript.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    transcript.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return transcript
