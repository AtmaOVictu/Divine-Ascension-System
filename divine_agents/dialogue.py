from typing import List, Sequence, Tuple, Optional
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    rounds: int = 1,
    emotion_adjustments: Optional[Sequence[Tuple[float, float]]] = None,
    tension_adjustments: Optional[Sequence[Tuple[float, float]]] = None,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        The participating agents.
    rounds : int, optional
        Number of dialogue rounds.
    emotion_adjustments : Sequence[Tuple[float, float]], optional
        Amounts by which to increase each agent's emotion each round.
    tension_adjustments : Sequence[Tuple[float, float]], optional
        Amounts by which to increase each agent's tension each round.
    """

    if emotion_adjustments is None:
        # default behaviour replicating previous single-round updates
        emotion_adjustments = [(0.8, 0.6)] + [(0.0, 0.0)] * (rounds - 1)
    if tension_adjustments is None:
        tension_adjustments = [(0.0, 0.0)] * rounds

    # ensure provided sequences have required length
    if len(emotion_adjustments) < rounds:
        emotion_adjustments = list(emotion_adjustments) + [
            (0.0, 0.0)
        ] * (rounds - len(emotion_adjustments))
    if len(tension_adjustments) < rounds:
        tension_adjustments = list(tension_adjustments) + [
            (0.0, 0.0)
        ] * (rounds - len(tension_adjustments))

    lines: List[str] = []
    for idx in range(rounds):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        e1, e2 = emotion_adjustments[idx]
        t1, t2 = tension_adjustments[idx]
        if e1:
            agent1.update_emotion(e1)
        if t1:
            agent1.update_tension(t1)
        state1 = agent1.transition()

        if e2:
            agent2.update_emotion(e2)
        if t2:
            agent2.update_tension(t2)
        state2 = agent2.transition()

        lines.append(f"{agent1.name} prehaja v stanje: {state1}")
        lines.append(f"{agent2.name} prehaja v stanje: {state2}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
