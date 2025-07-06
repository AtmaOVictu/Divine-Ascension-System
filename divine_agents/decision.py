class DecisionMaker:
    """Logic to decide an agent's next state based on emotion and tension."""

    def __init__(self, agent):
        self.agent = agent

    def decide_transition(self) -> str:
        """Return the next state without mutating the agent."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            if self.agent.state == "Ego":
                return "Jaz"
            if self.agent.state == "Jaz":
                return "Enotnost"
        return self.agent.state
