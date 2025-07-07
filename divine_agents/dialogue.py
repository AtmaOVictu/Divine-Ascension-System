from typing import List
from .agent import Agent
from .manager import ManagerAgent, SubAgent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Emotions are updated during the debate which might trigger state
    transitions. All actions are logged via sub agents.
    """
    manager = ManagerAgent("MainManager")
    manager.add_agent(agent1)
    manager.add_agent(agent2)

    # attach helpers for logging
    s1 = SubAgent("helper1", agent1)
    s2 = SubAgent("helper2", agent2)
    agent1.add_sub_agent(s1)
    agent2.add_sub_agent(s2)

    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # both agents react emotionally to the discussion
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    # manager coordinates the potential transitions
    manager.manage_transitions()

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # return dialogue lines along with logs from helpers
    lines.extend(s1.logs)
    lines.extend(s2.logs)

    return lines
