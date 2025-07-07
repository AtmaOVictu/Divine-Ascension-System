from typing import List

from .agent import Agent
from .keylock import Key, Lock


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 uses a key to unlock a lock despite low emotion
    agent1.add_lock(Lock("Emotion Lock", lock_type="emotion"))
    agent1.add_key(Key("Emotion Key", key_type="emotion"))
    agent1.update_emotion(0.2)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 relies on tension threshold
    agent2.add_lock(Lock("Task Lock", lock_type="task_complete"))
    agent2.add_key(Key("Task Key", key_type="task_complete"))
    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
