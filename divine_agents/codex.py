from typing import List
from .agent import Agent


class CriticalReflectionAgent(Agent):
    """Agent capable of recording reflections on past transitions."""

    def reflect_on_actions(self) -> None:
        if "Ego" in self.history:
            self.history.append(
                f"{self.name} is reflecting on Ego state: How does this affect my perception of reality?"
            )
        if "Jaz" in self.history:
            self.history.append(
                f"{self.name} is reflecting on Jaz state: Am I progressing towards unity?"
            )
        if "Enotnost" in self.history:
            self.history.append(
                f"{self.name} is reflecting on Enotnost state: Have I reached a state of transcendence?"
            )
        self.history.append(f"Critical reflection completed for {self.name}.")


class LoveHatePhilosophicalAgent(CriticalReflectionAgent):
    """Agent that evaluates love and hate influence on philosophical stance."""

    def evaluate_emotional_impact(self) -> None:
        if self.love > self.hate:
            self.history.append(
                f"{self.name} is motivated by love, seeking harmony and unity."
            )
        elif self.hate > self.love:
            self.history.append(
                f"{self.name} is motivated by hate, creating conflict and division."
            )
        else:
            self.history.append(
                f"{self.name} is in a state of emotional equilibrium, seeking balance."
            )


class CodexSimulation:
    """Simulation orchestrating philosophical transitions for multiple agents."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def run_simulation(self) -> None:
        for agent in self.agents:
            agent.transition()
            agent.philosophical_analysis()
            if isinstance(agent, CriticalReflectionAgent):
                agent.reflect_on_actions()
            if isinstance(agent, LoveHatePhilosophicalAgent):
                agent.evaluate_emotional_impact()

    def print_agents_philosophical_context(self) -> List[str]:
        contexts = []
        for agent in self.agents:
            contexts.append(
                f"{agent.name}'s philosophical context: {agent.philosophical_context.get(agent.name, 'No analysis')}"
            )
        return contexts
