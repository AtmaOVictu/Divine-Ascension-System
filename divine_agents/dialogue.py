from typing import List
from .agent import Agent
from .processes import Affirmation, Negation


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    # initial affirmation of existence
    lines.append(Affirmation.affirm_existence(agent1))
    lines.append(Affirmation.affirm_existence(agent2))

    # initial philosophical stance
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # emotions rise during dialogue, leading to transitions
    agent1.update_emotion(0.8)
    agent1.transition()
    lines.append(Affirmation.affirm_transition(agent1))

    agent2.update_emotion(0.6)
    agent2.transition()
    lines.append(Affirmation.affirm_transition(agent2))

    # optional negation event for dramatic effect
    Negation.negate_state(agent1)
    lines.append(Affirmation.affirm_transition(agent1))

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
