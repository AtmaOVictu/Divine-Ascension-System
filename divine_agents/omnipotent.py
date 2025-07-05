from typing import List
from .agent import Agent


class OmnipotentAgent(Agent):
    """Agent capable of supervising and guiding others."""

    def __init__(self, name: str, state: str = "Ego"):
        super().__init__(name, state)
        self.supervision_scope: List[Agent] = []
        self.analysis_report: List[str] = []

    def assign_supervision(self, agents: List[Agent]) -> None:
        """Assign agents for supervision."""
        self.supervision_scope = agents
        names = [agent.name for agent in agents]
        self.analysis_report.append(f"Assigned supervision over: {names}")

    def analyze_agents(self) -> None:
        """Analyze supervised agents and record observations."""
        for agent in self.supervision_scope:
            last_state = agent.history[-1] if agent.history else agent.state
            if agent.emotion < 0:
                self.analysis_report.append(
                    f"Agent {agent.name} shows negative emotions in {last_state}."
                )
            elif agent.emotion > 0:
                self.analysis_report.append(
                    f"Agent {agent.name} shows positive emotions in {last_state}."
                )
            else:
                self.analysis_report.append(
                    f"Agent {agent.name} has neutral emotions in {last_state}."
                )
            if agent.tension > 0.7:
                self.analysis_report.append(
                    f"Agent {agent.name} has high tension and may require guidance."
                )

    def provide_feedback(self) -> str:
        """Return collected analysis as a feedback string."""
        if not self.analysis_report:
            return "No analysis performed."
        return "\n".join(self.analysis_report)

    def control_transition(self, agent: Agent) -> str:
        """Force agent transition based on tension or emotion."""
        if agent.tension > 0.7:
            agent.state = "Enotnost"
        elif agent.emotion < -0.5:
            agent.state = "Ego"
        agent.history.append(agent.state)
        return agent.state
