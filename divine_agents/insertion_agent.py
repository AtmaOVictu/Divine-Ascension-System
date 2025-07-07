from .agent import Agent

class InsertionAgent:
    """Agent that can insert states, data, or behaviors into another agent."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def insert_state(self, new_state: str) -> None:
        """Insert a new state into Agent.STATES if not already present."""
        if new_state not in Agent.STATES:
            Agent.STATES = Agent.STATES + (new_state,)

    def insert_data(self, data: dict) -> None:
        """Insert new data into the agent's knowledge base."""
        if not hasattr(self.agent, "knowledge"):
            self.agent.knowledge = {}
        self.agent.knowledge.update(data)

    def modify_behavior(self, behavior: str) -> None:
        """Add a new behavior to the agent."""
        if not hasattr(self.agent, "behaviors"):
            self.agent.behaviors = []
        self.agent.behaviors.append(behavior)

