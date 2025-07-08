from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    def format_agent_line(agent: Agent) -> str:
        return (
            f"{agent.name} ({agent.state}, emotion={agent.emotion:.2f}, "
            f"tension={agent.tension:.2f}): {agent.respond('Kaj je resnica?')}"
        )

    lines.append(format_agent_line(agent1))
    lines.append(format_agent_line(agent2))

    for sub in getattr(agent1, "subagents", []):
        lines.append(sub.interact())
    for sub in getattr(agent2, "subagents", []):
        lines.append(sub.interact())

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(format_agent_line(agent1))
    lines.append(format_agent_line(agent2))
    return lines
