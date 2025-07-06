from typing import List, Optional
from .agent import Agent
from .versioning import VersionLogger


def philosophical_dialogue(
    agent1: Agent, agent2: Agent, logger: Optional[VersionLogger] = None
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    new_state1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
    if logger:
        logger.log_version_change(1.0, f"{agent1.name} transitioned to {new_state1}")

    agent2.update_emotion(0.6)
    new_state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")
    if logger:
        logger.log_version_change(1.0, f"{agent2.name} transitioned to {new_state2}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
