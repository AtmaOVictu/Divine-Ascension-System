from typing import List, Optional

from .agent import Agent
from .recorder import ShortEgoRecorder


def philosophical_dialogue(
    agent1: Agent, agent2: Agent, recorder: Optional[ShortEgoRecorder] = None
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # emotional reactions
    agent1.update_emotion(0.8)
    if recorder:
        recorder.record_transition(agent1)
    else:
        agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6)
    if recorder:
        recorder.record_transition(agent2)
    else:
        agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # follow-up responses reflecting new states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

