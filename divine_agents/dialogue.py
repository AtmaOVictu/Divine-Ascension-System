from typing import List, Optional
from .agent import Agent
from .nonliving import NonLivingEntity


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    nonliving: Optional[List[NonLivingEntity]] = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    If non-living entities are provided, their descriptions are included at the
    end of the dialogue.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    if nonliving:
        lines.extend(NonLivingEntity.list_entities(nonliving))

    return lines
