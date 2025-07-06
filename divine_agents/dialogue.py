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


def dynamic_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate an emotion driven debate between two agents.

    The agents update their emotion which in turn influences their tension. If
    either metric crosses the transition thresholds defined in
    :py:meth:`Agent.transition`, the agent will change ontological state. The
    resulting conversation reflects these changes.
    """

    discussion: List[str] = []

    # Initial statements based on starting states
    discussion.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    discussion.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts emotionally to Agent2's argument
    agent1.update_emotion(0.6)
    discussion.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    discussion.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")

    # Agent2 becomes even more engaged in the debate
    agent2.update_emotion(0.8)
    discussion.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    discussion.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return discussion
