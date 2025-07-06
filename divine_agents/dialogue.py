"""Dialogue utilities for philosophical agent conversations."""
from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotion."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional shift leading to possible transitions
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines


def forced_usage_demo() -> List[str]:
    """Demonstrate container-based processing."""
    from .containers import AwarenessContainer, OppositionContainer, TransitionContainer

    awareness = AwarenessContainer()
    opposition = OppositionContainer()
    transition = TransitionContainer(awareness, opposition)

    transition.run()
    lines = [
        f"Awareness state: {awareness.run()}",
        f"Opposition state: {opposition.run()}"
    ]
    return lines
