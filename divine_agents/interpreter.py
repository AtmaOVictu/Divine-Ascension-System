from .agent import Agent


class CodeInterpreter:
    """Interprets data and triggers actions like state transitions."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def interpret_decision(self, data):
        """Decide on state transitions based on agent tension/emotion."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            return self.agent.transition()
        return self.agent.state
