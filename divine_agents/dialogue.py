from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion("anger", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("fear", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Run a multi-round debate influenced by emotions."""
    conversation: List[str] = []
    for _ in range(rounds):
        conversation.append(
            f"{agent1.name} ({agent1.state}, {agent1.emotional_state}): "
            f"{agent1.respond('Kaj je resnica?')}"
        )
        conversation.append(
            f"{agent2.name} ({agent2.state}, {agent2.emotional_state}): "
            f"{agent2.respond('Kaj je resnica?')}"
        )

        # agents react to each other's statements
        agent1.interact(agent2)
        agent2.interact(agent1)

        prev1, prev2 = agent1.state, agent2.state
        state1 = agent1.transition()
        state2 = agent2.transition()
        if prev1 != state1:
            conversation.append(f"{agent1.name} prehaja v stanje: {state1}")
        if prev2 != state2:
            conversation.append(f"{agent2.name} prehaja v stanje: {state2}")

    return conversation
