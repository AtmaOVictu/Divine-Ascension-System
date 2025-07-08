from typing import List
from .agent import Agent


def continuous_learning_cycle(agent1: Agent, agent2: Agent, emotion1: str, emotion2: str, time_step: float = 1.0) -> List[str]:
    """Run a single interaction updating emotions and tension."""
    # Adjust emotional intensity
    agent1.update_emotion(0.8 if emotion1 == "anger" else 0.2)
    agent2.update_emotion(0.8 if emotion2 == "anger" else 0.2)

    # Possibly transition states
    agent1.transition()
    agent2.transition()

    # Decay tension for both agents
    agent1.decay_tension(emotion1, time_step)
    agent2.decay_tension(emotion2, time_step)

    return [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]
