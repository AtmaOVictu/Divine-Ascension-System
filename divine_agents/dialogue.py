from typing import List
import random
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


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Run multiple dialogue rounds with emotional influence and transitions."""
    dialogue = []
    for i in range(rounds):
        dialogue.extend(philosophical_dialogue(agent1, agent2))
        for ag in (agent1, agent2):
            label = random.choice(["strah", "veselje", "jeza"])
            ag.feel(label, random.uniform(0.3, 0.9))
            ag.transition()
        dialogue.append(f"--- Krog {i + 1} zaključen ---")
    return dialogue
