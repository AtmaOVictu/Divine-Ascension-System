class DecisionMaker:
    """Handles state transitions and belief updates for an Agent."""
    def __init__(self, agent):
        self.agent = agent

    def decide_transition(self):
        """Determine the next state based on tension and emotion."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            if self.agent.state == "Ego":
                return "Jaz"
            if self.agent.state == "Jaz":
                return "Enotnost"
        return self.agent.state

    def evolve_beliefs(self):
        """Placeholder for evolving an agent's belief system."""
        pass
