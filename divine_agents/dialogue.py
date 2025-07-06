"""Dialogue utilities for divine agents."""

from concurrent.futures import ProcessPoolExecutor
from typing import Iterable, List, Tuple

from .agent import Agent
from .enums import Emotion


def _dialogue_pair(pair: Tuple[Agent, Agent]) -> List[str]:
    a1, a2 = pair
    lines = [
        f"{a1.name} ({a1.state.value}): {a1.respond('Kaj je resnica?')}",
        f"{a2.name} ({a2.state.value}): {a2.respond('Kaj je resnica?')}",
    ]

    a1.update_emotion(Emotion.FEAR, 0.8)
    lines.append(f"{a1.name} prehaja v stanje: {a1.transition().value}")

    a2.update_emotion(Emotion.JOY, 0.6)
    lines.append(f"{a2.name} prehaja v stanje: {a2.transition().value}")

    lines.append(f"{a1.name}: {a1.respond('Kaj je resnica?')}")
    lines.append(f"{a2.name}: {a2.respond('Kaj je resnica?')}")
    return lines


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    return _dialogue_pair((agent1, agent2))


def parallel_dialogues(pairs: Iterable[Tuple[Agent, Agent]]) -> List[List[str]]:
    """Run multiple dialogues concurrently using processes."""
    with ProcessPoolExecutor() as exe:
        futures = [exe.submit(_dialogue_pair, p) for p in pairs]
        return [f.result() for f in futures]
