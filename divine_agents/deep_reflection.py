from .agent import Agent
from .shared_memory import SharedMemory


class DeepReflection:
    """Perform deeper reflection using shared history."""

    def __init__(self, agent: Agent, memory: SharedMemory) -> None:
        self.agent = agent
        self.memory = memory

    def perform(self) -> str:
        """Trigger a state change based on historical insight."""
        history = self.memory.retrieve_history()
        if history:
            self.agent.update_tension(0.8)
            return self.agent.transition()
        return self.agent.state
