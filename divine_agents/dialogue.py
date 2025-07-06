from typing import List, Optional
from .agent import Agent
from .data import DataHarvester
from .logger import CodeLogger
from .interpreter import CodeInterpreter


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    harvester: Optional[DataHarvester] = None,
    logger: Optional[CodeLogger] = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The function records data and logs events if corresponding helpers are
    provided. Agents may transition states based on their emotional updates.
    """
    lines: List[str] = []

    for agent in (agent1, agent2):
        if harvester:
            harvester.collect_data(agent, "start")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    if logger:
        logger.log_event(f"{agent1.name} emotion set to {agent1.emotion}")
    if harvester:
        harvester.collect_data(agent1, "emotion_update")
    new_state1 = CodeInterpreter(agent1).interpret_decision(harvester.data if harvester else [])
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")

    agent2.update_emotion(0.6)
    if logger:
        logger.log_event(f"{agent2.name} emotion set to {agent2.emotion}")
    if harvester:
        harvester.collect_data(agent2, "emotion_update")
    new_state2 = CodeInterpreter(agent2).interpret_decision(harvester.data if harvester else [])
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
