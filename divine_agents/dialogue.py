from typing import List

from .agent import Agent
from .recorder import ShortEgoRecorder


def philosophical_dialogue(agent1: Agent, agent2: Agent, recorder: ShortEgoRecorder | None = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    new_state = agent1.transition()
    if recorder:
        recorder.record_transition(agent1, new_state)
    lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

    agent2.update_emotion(0.6)
    new_state = agent2.transition()
    if recorder:
        recorder.record_transition(agent2, new_state)
    lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
