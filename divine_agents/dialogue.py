from typing import List

from .agent import Agent
from .lock import Lock, Key


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue where emotions influence transitions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Attach locks and keys based on emotion conditions
    lock1 = Lock("State Lock", condition="emotion")
    lock2 = Lock("State Lock", condition="emotion")
    agent1.add_lock(lock1)
    agent2.add_lock(lock2)
    agent1.add_key(Key("Emotion Key", key_type="emotion"))
    agent2.add_key(Key("Emotion Key", key_type="emotion"))

    # Update emotions which raise tension and trigger unlocking
    agent1.update_emotion(agent1.emotion + 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(agent2.emotion + 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines

