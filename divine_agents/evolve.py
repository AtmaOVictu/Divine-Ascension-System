from .agent import Agent


def evolve_to_unity(agent: Agent, step_emotion: float = 0.8) -> Agent:
    """Advance the agent until it reaches the final ontological state."""
    while not agent.is_complete():
        agent.advance(step_emotion)
    return agent
