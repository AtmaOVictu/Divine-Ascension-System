class InsertionAgent:
    """Provides dynamic modifications for an Agent."""

    def __init__(self, agent):
        self.agent = agent

    def insert_state(self, new_state: str) -> None:
        """Insert a new state into the agent's state machine."""
        if new_state not in self.agent.STATES:
            self.agent.STATES = self.agent.STATES + (new_state,)

    def insert_data(self, data: dict) -> None:
        """Insert new knowledge into the agent."""
        if not hasattr(self.agent, "knowledge"):
            self.agent.knowledge = {}
        self.agent.knowledge.update(data)

    def modify_behavior(self, behavior: str) -> None:
        """Append a new behavior for the agent."""
        if not hasattr(self.agent, "behaviors"):
            self.agent.behaviors = []
        self.agent.behaviors.append(behavior)

