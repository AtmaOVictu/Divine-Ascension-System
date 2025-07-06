from typing import List, Optional
from .agent import Agent
from .analytics import DataHarvester, CodeLogger


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    harvester: Optional[DataHarvester] = None,
    logger: Optional[CodeLogger] = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    def add_line(text: str) -> None:
        lines.append(text)
        if logger:
            logger.log_event(text)

    line1 = f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    add_line(line1)
    line2 = f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    add_line(line2)

    agent1.update_emotion(0.8)
    state1 = agent1.transition()
    add_line(f"{agent1.name} prehaja v stanje: {state1}")
    if harvester:
        harvester.collect_data({"agent": agent1.name, "state": state1})

    agent2.update_emotion(0.6)
    state2 = agent2.transition()
    add_line(f"{agent2.name} prehaja v stanje: {state2}")
    if harvester:
        harvester.collect_data({"agent": agent2.name, "state": state2})

    add_line(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    add_line(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
