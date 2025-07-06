"""Dialogue utilities for philosophical interactions."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(agent1.express_truth())
    lines.append(agent2.express_truth())

    agent1.update_emotion(1.0, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(agent1.express_truth())
    lines.append(agent2.express_truth())
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a more elaborate debate influenced by emotion and tension."""
    history = []
    history.append(agent1.express_truth())
    history.append(agent2.express_truth())

    # increase tension through emotional interaction
    agent1.update_emotion(0.9, "fear")
    agent1.transition()
    history.append(agent1.express_truth())

    agent2.update_emotion(0.6, "anger")
    agent2.transition()
    history.append(agent2.express_truth())

    return history
