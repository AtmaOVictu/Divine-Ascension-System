from typing import List
from .agent import Agent
from .system import Command, DynamicAdjustment


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    adjustment = DynamicAdjustment()

    ask_truth = Command("ask_truth", lambda: "Kaj je resnica?")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(ask_truth.execute())}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(ask_truth.execute())}")

    # Emotional reactions trigger tension adjustments
    agent1.update_emotion(0.8, "fear")
    lines.append(adjustment.adjust_tension(agent1, agent1.tension))
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(adjustment.adjust_tension(agent2, agent2.tension))
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(ask_truth.execute())}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(ask_truth.execute())}")

    return [line for line in lines if line]
