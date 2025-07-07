"""Utilities for simulating philosophical dialogues between agents."""
from __future__ import annotations

from typing import List

from .agent import Agent
from .lock import Lock, Key


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Attach locks and keys governing state transitions
    lock1 = Lock("state_lock_1", condition="emotion")
    lock2 = Lock("state_lock_2", condition="emotion")
    agent1.add_lock(lock1)
    agent2.add_lock(lock2)
    agent1.add_key(Key("emotion_key_1", key_type="emotion"))
    agent2.add_key(Key("emotion_key_2", key_type="emotion"))

    # Emotions escalate as dialogue progresses
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
