from .agent import Agent

class TehtniRazlog:
    """EtnegA helper that weighs reasons for an agent's transition."""

    THRESHOLD_HIGH = 0.7
    THRESHOLD_LOW = 0.3

    def __init__(self, agent: Agent):
        self.agent = agent

    def calculate_reason(self) -> float:
        """Return weighted reason based on tension and emotion."""
        return self.agent.tension * self.agent.emotion

    def decide(self) -> str:
        """Provide guidance on whether a transition should occur."""
        value = self.calculate_reason()
        if value > self.THRESHOLD_HIGH:
            return "Prehod je nujen, vendar premislimo o posledicah."
        if value > self.THRESHOLD_LOW:
            return "Prehod ni nujen, vendar raziskujmo možnost."
        return "Prehod je nepotreben, zadržimo se v trenutnem stanju."

    def reflect(self) -> str:
        """Apply decision and transition the agent when necessary."""
        decision = self.decide()
        if "nujen" in decision:
            self.agent.transition()
        return decision

    def __repr__(self) -> str:
        return f"TehtniRazlog(agent={self.agent.name}, state={self.agent.state})"
