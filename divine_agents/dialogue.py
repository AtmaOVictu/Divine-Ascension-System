from typing import Dict, List, Optional, Sequence
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    adjustments: Optional[Sequence[Dict[str, float]]] = None,
    prompts: Optional[Sequence[str]] = None,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        The first agent participating in the dialogue.
    agent2 : Agent
        The second agent participating in the dialogue.
    adjustments : Optional sequence of dictionaries
        If provided, each dictionary may contain ``emotion1``, ``tension1``,
        ``emotion2`` and ``tension2`` values applied to the agents after the
        initial responses for that step.
    prompts : Optional sequence of strings
        Questions posed to both agents in order. If omitted, a default prompt
        ``"Kaj je resnica?"`` is used for each step.

    Returns
    -------
    List[str]
        A list of dialogue lines representing the interaction and any state
        transitions.
    """

    default_prompt = "Kaj je resnica?"
    num_steps = max(
        len(prompts) if prompts else 1,
        len(adjustments) if adjustments else 0,
    )

    lines: List[str] = []

    for step in range(num_steps):
        prompt = prompts[step] if prompts and step < len(prompts) else default_prompt

        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(prompt)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(prompt)}")

        if adjustments and step < len(adjustments):
            adj = adjustments[step]
            if "emotion1" in adj:
                agent1.update_emotion(adj["emotion1"])
            if "tension1" in adj:
                agent1.update_tension(adj["tension1"])
            if "emotion2" in adj:
                agent2.update_emotion(adj["emotion2"])
            if "tension2" in adj:
                agent2.update_tension(adj["tension2"])

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name}: {agent1.respond(prompt)}")
        lines.append(f"{agent2.name}: {agent2.respond(prompt)}")

    return lines
