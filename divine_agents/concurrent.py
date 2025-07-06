"""Parallel execution helpers for agent dialogues."""

from concurrent.futures import ThreadPoolExecutor
from typing import Iterable, List, Sequence, Tuple

from .agent import Agent
from .dialogue import philosophical_dialogue


Pair = Tuple[Agent, Agent]


def run_parallel_dialogues(pairs: Sequence[Pair]) -> List[List[str]]:
    """Run multiple dialogues in parallel threads.

    Parameters
    ----------
    pairs:
        Sequence of ``(Agent, Agent)`` tuples representing dialogues.

    Returns
    -------
    List of dialogue transcripts corresponding to ``pairs`` order.
    """
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda p: philosophical_dialogue(p[0], p[1]), pairs))
    return results


__all__ = ["run_parallel_dialogues", "Pair"]
