from typing import List
from .agent import Agent


def _maybe_track(agent: Agent, data_type: str, source: str) -> None:
    """Helper to call track_data_usage if supported."""
    if hasattr(agent, "track_data_usage"):
        agent.track_data_usage(data_type, source)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    _maybe_track(agent1, "dialogue_start", "question")
    _maybe_track(agent2, "dialogue_start", "question")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    agent1_state = agent1.transition()
    _maybe_track(agent1, "state_transition", agent1_state)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1_state}")

    agent2.update_emotion(0.6)
    agent2_state = agent2.transition()
    _maybe_track(agent2, "state_transition", agent2_state)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2_state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    _maybe_track(agent1, "dialogue_end", "answer")
    _maybe_track(agent2, "dialogue_end", "answer")
    return lines
