from .agent import Agent
from .frequency import AgentFrekvenca


class AgentZvok:
    """Connects frequency detection to ontological state transitions via sound."""

    def __init__(self, agent: Agent, frekvenca_agent: AgentFrekvenca | None = None) -> None:
        self.agent = agent
        self.frekvenca_agent = frekvenca_agent or AgentFrekvenca()
        self.log = []

    def process(self, frequency: float) -> str:
        """Detect frequency and update the agent's state if tension threshold is reached."""
        status = self.frekvenca_agent.detect(self.agent.state, frequency)
        if frequency > 1.5:
            # Higher frequency increases tension leading to possible transition
            self.agent.update_tension(1.0)
            new_state = self.agent.transition()
        else:
            new_state = self.agent.state
        self.log.append((frequency, status, new_state))
        return status

    def history(self):
        return self.log
