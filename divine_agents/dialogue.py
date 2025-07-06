from typing import List
from .agent import Agent
from .instrumentation import DataHarvester, CodeLogger


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    logger = CodeLogger()
    harvester = DataHarvester()

    lines: List[str] = []
    # Initial statements
    line1 = f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    line2 = f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    lines.extend([line1, line2])
    logger.log_event(line1)
    logger.log_event(line2)
    harvester.collect_data({'agent': agent1.name, 'state': agent1.state})
    harvester.collect_data({'agent': agent2.name, 'state': agent2.state})

    # Emotion updates trigger potential transitions
    agent1.update_emotion(0.8)
    transition1 = agent1.transition()
    logger.log_event(f"{agent1.name} transitioned to {transition1}")
    lines.append(f"{agent1.name} prehaja v stanje: {transition1}")

    agent2.update_emotion(0.6)
    transition2 = agent2.transition()
    logger.log_event(f"{agent2.name} transitioned to {transition2}")
    lines.append(f"{agent2.name} prehaja v stanje: {transition2}")

    # Closing statements
    closing1 = f"{agent1.name}: {agent1.respond('Kaj je resnica?')}"
    closing2 = f"{agent2.name}: {agent2.respond('Kaj je resnica?')}"
    lines.extend([closing1, closing2])
    logger.log_event(closing1)
    logger.log_event(closing2)
    harvester.collect_data({'agent': agent1.name, 'state': agent1.state})
    harvester.collect_data({'agent': agent2.name, 'state': agent2.state})
    return lines
