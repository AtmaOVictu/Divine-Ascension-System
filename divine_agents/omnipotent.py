from __future__ import annotations

from typing import List

from .agent import Agent


class OmnipotentAgent(Agent):
    """Agent with supervisory powers over other agents."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.criticality_level = 0
        self.supervision_scope: List[Agent] = []
        self.analysis_report: List[str] = []

    def assign_supervision(self, agents: List[Agent]) -> None:
        """Assign other agents to supervise."""
        self.supervision_scope = agents
        self.analysis_report.append(
            f"Assigned supervision over: {[agent.name for agent in agents]}"
        )

    def analyze_agents(self) -> None:
        """Analyze supervised agents and record findings."""
        for agent in self.supervision_scope:
            agent_state = agent.state
            if agent.tension > 0.7:
                self.analysis_report.append(
                    f"Agent {agent.name} has high tension in state {agent_state}."
                )
            if agent.emotion < 0:
                self.analysis_report.append(
                    f"Agent {agent.name} shows negative emotions."
                )
            elif agent.emotion > 0:
                self.analysis_report.append(
                    f"Agent {agent.name} shows positive emotions."
                )
            else:
                self.analysis_report.append(
                    f"Agent {agent.name} has neutral emotions."
                )

    def provide_feedback(self) -> str:
        """Return collected analysis feedback."""
        if not self.analysis_report:
            return "No agents under supervision."
        return "\n".join(self.analysis_report)

    def control_transition(self, agent: Agent) -> None:
        """Force agent transition based on tension or emotion."""
        if agent.tension > 0.7:
            agent.state = "Enotnost"
            agent.history.append(f"{self.name} directed {agent.name} to state: Enotnost")
        elif agent.emotion < -0.5:
            agent.state = "Ego"
            agent.history.append(f"{self.name} directed {agent.name} to state: Ego")


class AgentImprovement(OmnipotentAgent):
    """Provide improvement recommendations to agents."""

    def recommend_improvement(self, agent: Agent) -> str:
        if agent.emotion < -0.5:
            return (
                f"Agent {agent.name} needs to focus on reducing hate and improving cooperation."
            )
        if agent.emotion < 0.5:
            return (
                f"Agent {agent.name} needs to develop stronger positive emotional bonds (Love)."
            )
        return (
            f"Agent {agent.name} is progressing well, but should maintain emotional balance."
        )


class SystemAnalysis:
    """Analyze a collection of agents for overall system health."""

    def __init__(self, agents: List[Agent]) -> None:
        self.agents = agents
        self.analysis_report: List[str] = []

    def analyze_system(self) -> None:
        for agent in self.agents:
            if agent.tension > 0.7:
                self.analysis_report.append(f"Agent {agent.name} has high tension.")
            if agent.emotion < -0.5:
                self.analysis_report.append(
                    f"Agent {agent.name} is overwhelmed by negative emotions (Hate)."
                )
            else:
                self.analysis_report.append(
                    f"Agent {agent.name} has balanced emotions."
                )

    def get_system_feedback(self) -> str:
        return "\n".join(self.analysis_report)
