from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

from .box import AgentBox


def boxed_philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate dialogue while tracking integrity using AgentBox wrappers."""
    box1 = AgentBox(agent1)
    box2 = AgentBox(agent2)

    lines = []
    lines.append(f"{box1.agent.name} ({box1.agent.state}): {box1.agent.respond('Kaj je resnica?')}")
    lines.append(f"{box2.agent.name} ({box2.agent.state}): {box2.agent.respond('Kaj je resnica?')}")

    box1.update_agent(emotion=0.8)
    box1.transition_agent()
    lines.append(f"{box1.agent.name} prehaja v stanje: {box1.agent.state}")

    box2.update_agent(emotion=0.6)
    box2.transition_agent()
    lines.append(f"{box2.agent.name} prehaja v stanje: {box2.agent.state}")

    lines.append(f"{box1.agent.name}: {box1.agent.respond('Kaj je resnica?')}")
    lines.append(f"{box2.agent.name}: {box2.agent.respond('Kaj je resnica?')}")
    return lines
