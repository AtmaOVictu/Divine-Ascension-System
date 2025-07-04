import time
from typing import List

from .agent import Agent


class Environment:
    """Simple environment to track absolute and relative time."""

    def __init__(self) -> None:
        self.start = time.time()

    def now(self) -> float:
        """Return elapsed time since environment creation."""
        return time.time() - self.start


def timed_dialogue(agent1: Agent, agent2: Agent, env: Environment) -> List[str]:
    """Simulate dialogue with timestamps based on environment time."""
    lines = []
    lines.append(
        f"[{env.now():.2f}s] {agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"[{env.now():.2f}s] {agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"[{env.now():.2f}s] {agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"[{env.now():.2f}s] {agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"[{env.now():.2f}s] {agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"[{env.now():.2f}s] {agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
